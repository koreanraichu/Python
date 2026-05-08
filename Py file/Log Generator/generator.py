# 여기서 이벤트를 생성할겁니다. 근데 이제 몇 가지 규칙을 곁들인... 
# 1. 각 아이디는 6자리 정수형으로, 6자리가 안 될 경우 출력 시 앞에 비는 만큼 0으로 채운다. (예: 1234->001234)
# 2. 화합물 정보 확인, 검색 결과 조회, csv 다운로드는 검색이 반드시 선행되어야 한다. 
# 3. 같은 검색 아이디 내에서 csv 다운로드는 한 번만 하는 것으로 한다. (보통 필요한 것만 한번에 받죠...?) 단, 화합물 조회는 **검색 결과가 여러개라면** 여러 번 진행될 수 있다. 
# 4. 같은 사용자가 여러 개의 화합물을 검색할 수 있다. 예를 들어서, 한 사용자가 아세트아미노펜과 이부프로펜을 검색할 수 있다. 물론 검색 결과와 후행 이벤트 역시 다른 검색 ID에 대해서는 별개이다. 
# 5. 검색 ID가 같다면 검색어도 같다. 반대로 검색 ID가 다르다면 검색어도 다르다. 
# 6. 에러가 생겼을 때는 이벤트 아이디와 검색 아이디, 유저 아이디, 이벤트 타입, 에러 타입만 기록된다. 

# 렌덤 컴히얼
import random # 우리 이거 무작위로 만들어야됩니다 
import sqlite3 # db에 있던 그 친구
from datetime import datetime, timedelta # 시간도 이제 랜덤으로 만듭니다 

# 클래스에서 써야됨
conn = sqlite3.connect("events.db")
cursor = conn.cursor()

class EventGenerator: # OOP 서타일
    def __init__(self):
        self.conn = conn
        self.cursor = cursor
        self.search_id = 0 # 일단은 0 
        # 여기 있는 분자들은 약으로 쓰고 있는 분자들입니다. (진세노사이드는 인삼에 들어있는 사포닌)
        # 오타는 일부러 넣은겁니다. 대신 오타의 경우 후속 이벤트도 없고, 검색 결과 수도 0입니다. 
        # artemisinin: 오타입니다. artemisinin이 맞아요. 
        # nafroxen: 얘도 오타입니다. naproxen이 맞아요. 
        # acetaminopen: acetaminophen이 맞습니다. 
        # gentamycin: gentamicin이 맞습니다. 
        self.compounds = ["aspirin","ibuprofen","acetaminopen","acetaminophen","arteminisin","artemisinin","imatinib","nafroxen","ginsenoside","salicylic acid","naproxen","fluoxetine","thalidomide","duloxetine","gentamycin","gentamicin","rifampicin"]
        self.compound_results = { # 검색 결과 고정해야 합니다. 똑같은 검색어로 똑같은 DB 뒤져서 누구는 100건 누구는 200건 이건 에바입니다. 
            "aspirin": 120,
            "ibuprofen": 85,
            "acetaminophen": 143,
            "artemisinin": 67,
            "imatinib": 41,
            "ginsenoside": 23,
            "salicylic acid": 98,
            "naproxen": 74,
            "fluoxetine": 56,
            "thalidomide": 12,
            "duloxetine": 37,
            "gentamicin": 29,
            "rifampicin": 44
        }
        self.typo_corrections = { # 룰 7. 오타의 경우 검색 결과가 0개/룰 8. 오타때문에 결과가 0이 나왔다면, 그 사용자는 제대로 된 철자를 사용해서 다시 검색한다. (하다가 추가됨)
            "acetaminopen": "acetaminophen",
            "arteminisin": "artemisinin",
            "nafroxen": "naproxen",
            "gentamycin": "gentamicin"
        }
        self.current_search_id = 1
    
    # 시간 랜덤 생성기 
    def random_timestamp(self):
        start_date = datetime(2026, 5, 1)
        end_date = datetime(2026, 5, 8)
        delta = end_date - start_date
        random_seconds = random.randint(0, int(delta.total_seconds()))
        random_time = start_date + timedelta(seconds=random_seconds)
        return random_time.strftime("%Y-%m-%d %H:%M:%S")

    # 이벤트 생성기
    def insert_event(self,search_id,user_id,event_type,query=None,result_count=None,compound_id=None,error_type=None):
        event = {
            "search_id": f"{search_id:06d}",
            "user_id": f"{user_id:06d}",
            "event_type": event_type,
            "query": query,
            "result_count": result_count,
            "compound_id": (
                f"{compound_id:06d}"
                if compound_id is not None
                else None
            ),
            "error_type": error_type,
            "timestamp": self.random_timestamp()
        }

        # SQL에 넣으려면 INSERT INTO가 필요합니다. 
        insert_query = """
            INSERT INTO events (
                search_id,
                user_id,
                event_type,
                query,
                result_count,
                compound_id,
                error_type,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
        
        self.cursor.execute(
            insert_query,
            (
                event["search_id"],
                event["user_id"],
                event["event_type"],
                event["query"],
                event["result_count"],
                event["compound_id"],
                event["error_type"],
                event["timestamp"]
            )
        )

        # 지금은 과제니까 하나하나 커밋하는거지만, 착한 엔지니어 여러분들은 batch commit을 써주세요 
        # 커밋 한땀한땀 하는것도 다 시간 걸려요. 
        self.conn.commit() 

        return event
    
    # 검색에서 후행 이벤트 파생시킬 애 
    def generate_search_flow(self):
        user_id = random.randint(1, 999999) # 사용자 아이디: 랜덤입니다. 마치 포켓몬 게임의 트레이너 아이디같은 것... (랜덤임)
        query = random.choice(self.compounds) # 사용자의 검색어 
        search_id = self.current_search_id # 검색 아이디
        self.current_search_id += 1
        if query in self.typo_corrections: # 오타났으면 
            result_count = 0 # 결과 0개 (룰 7에 의거함)
        else:
            result_count = self.compound_results[query] # 아니면 개수 출력하시고 
        event = self.insert_event(search_id,user_id,"search",query=query,result_count=result_count) # 이벤트 생성
        events = [event]

        if result_count > 0:
            self.generate_followup_events(events, search_id, user_id, query, result_count) # 후행 이벤트 따로 뺐습니다 
        else:
            result_view_event = self.insert_event(search_id, user_id, "result_view", query=query, result_count=0)
            events.append(result_view_event)

        # 룰 8. 오타때문에 결과가 0이 나왔다면, 그 사용자는 제대로 된 철자를 사용해서 다시 검색한다.
        if query in self.typo_corrections:

            corrected_query = self.typo_corrections[query] # 오타때문에 결과가 안 떴으니 철자를 교정해서 재검색을 해줍니다 

            corrected_search_id = self.current_search_id
            self.current_search_id += 1 # 사용자는 같지만 검색은 다시 하는거라서 아이디는 다름 

            corrected_result_count = self.compound_results[corrected_query] # 철자 정정했으니까 다시 결과가 나오겠죠? 
            corrected_event = self.insert_event(corrected_search_id, user_id, "search", query=corrected_query, result_count=corrected_result_count) # 그럼 다시 생성해야겠죠? 
            events.append(corrected_event)
            self.generate_followup_events(events, corrected_search_id, user_id, corrected_query, corrected_result_count)
        
        return events
    
    # 원래 한 덩어리였던 후행 이벤트를 따로 뺐습니다. 
    def generate_followup_events(self, events, search_id, user_id, query, result_count):
        if random.random() < 0.95: # 5% 확률로 에러가 당신을 반깁니다 
            # 검색 결과 조회
            result_view_event = self.insert_event(search_id, user_id, "result_view", query=query, result_count=result_count)
            events.append(result_view_event)

            # 검색 결과에서 개별 화합물 결과를 보겠죠? 
            chemical_view_count = random.randint(1, min(result_count, 5))
            for _ in range(chemical_view_count):
                # 하지만 1번만 보라는 법은 없죠? 
                compound_id = random.randint(1, result_count)
                chemical_event = self.insert_event(search_id, user_id, "chemical_view", query=query, compound_id=compound_id)
                events.append(chemical_event)

            # 다운로드(CSV로)->다운로드는 한번만 합니다. 
            if random.random() < 0.7: # 실패할 확률 있음(30%)
                csv_event = self.insert_event(search_id, user_id, "csv_download", query=query)
                events.append(csv_event)
            else:
                error_event = self.insert_event(search_id, user_id, "error", error_type="csv_download_failed")
                events.append(error_event)
        else: 
            error_event = self.insert_event(search_id, user_id, "error", error_type="result_page_timeout")
            events.append(error_event)

generator = EventGenerator()

for _ in range(1000):
    event = generator.generate_search_flow()

print("Generation complete") # 확인용입니다. 다되면 다됐음 하는 뭐 그런 