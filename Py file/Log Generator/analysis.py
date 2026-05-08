# 자 그래서 여기서는 뭘 할거냐! 집계분석 하랬으니까 집계분석 할거예요... (간단)

import sqlite3 # SQLite 
import matplotlib.pyplot as plt

# 그래프 전역 설정 구역
# 그래프를 그리기 위한 기본 설정
plt.rcParams["figure.figsize"] = (10, 5) 
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

# 1. 에러 이벤트 비율 
# 전체 비율 비율이랑 각 에러 이벤트별 발생 횟수 두개를 볼겁니다. 그러니까 이걸로 
# 1) 전체 중 에러 비율이 얼마구나 
# 2) 이 에러가 많이 일어났구나 
# 이 두가지를 보고자 하는겁니다. 

# 전체 이벤트 중 에러 비율 
error_rate_query = """
    SELECT ROUND(COUNT(CASE WHEN event_type = 'error' THEN 1 END) * 100.0 / COUNT(*),2) AS error_rate FROM events;
"""

# 각 에러 이벤트의 발생 횟수
error_type_query = """
    SELECT error_type, COUNT(*) AS error_count FROM (SELECT * FROM events WHERE event_type = 'error') AS error GROUP BY error_type ORDER BY error_count DESC;
"""

cursor.execute(error_rate_query)
result = cursor.fetchone()

print(f"에러 이벤트 비율: {result[0]}%") # 전체 이벤트 비율 

cursor.execute(error_type_query)
result = cursor.fetchall()

print("="*30) # 구분선
for row in result:
    print(f"에러 이벤트명: {row[0]}, 발생횟수 {row[1]}") # 각 이벤트의 발생횟수 

# 2. 어떤 검색어가 많이 검색됐는가? 
# 여기서는 그냥 음 이런 검색어들을 검색했군 하나+뭔 오타를 이렇게 냈어 하나 가겠습니다. 

# 음 이런 검색어를 많이 찾았군 
search_query = """
    SELECT query, COUNT(*) AS search_count FROM events WHERE event_type = 'search' GROUP BY query ORDER BY search_count DESC;
"""

cursor.execute(search_query)
result = cursor.fetchall()

print("="*30)
for row in result:
    print(f"검색어: {row[0]}, 검색 횟수 {row[1]}") # 각 검색어별 검색 횟수

# 음 여기서 오타가 많았군
mistake_query = """
    SELECT query, COUNT(*) AS mistake_count FROM (SELECT * FROM events WHERE result_count = 0 AND event_type = 'search') AS mistake GROUP BY query ORDER BY mistake_count DESC;
"""

cursor.execute(mistake_query)
result = cursor.fetchall()

print("="*30)
for row in result:
    print(f"검색어: {row[0]}, 오타 횟수 {row[1]}") # 오타 집결

# 3. 시간대별 이벤트 발생 횟수
time_query = """
    SELECT strftime('%H', timestamp) AS hour, event_type, COUNT(*) AS event_count FROM events GROUP BY hour, event_type ORDER BY hour, event_type;
"""

cursor.execute(time_query)
result = cursor.fetchall()

print("="*30)
for hour, event, count in result:
    print(f"{hour}시 | {event} {count}회") # 몇시에 어떤 이벤트가 몇회?

# 시각화 ZONE
# 아... 주피터 마렵네... 

# 1. 시간대별 이벤트 횟수 
query = """
    SELECT strftime('%H', timestamp) AS hour, COUNT(*) AS cnt FROM events GROUP BY hour ORDER BY hour;
"""

cursor.execute(query)
rows = cursor.fetchall()

hours = [r[0] for r in rows]
counts = [r[1] for r in rows]

plt.plot(hours, counts, marker='o')
plt.title("Hourly Event Distribution")
plt.xlabel("Hour")
plt.ylabel("Events")
plt.xticks(rotation=0)
plt.grid(True)

plt.savefig("Hourly Event Distribution.png")
plt.close()

# 에러 비율 
query = """
    SELECT error_type, COUNT(*) FROM events WHERE event_type = 'error' GROUP BY error_type;
"""

cursor.execute(query)
rows = cursor.fetchall()

labels = [r[0] for r in rows]
sizes = [r[1] for r in rows]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Error Rate")

plt.savefig("Error Rate.png")
plt.close()