# 아 이게요... 
# 개발용으로 쓰는 컴퓨터가 따로 있는데 거기에는 도커 오라클 파이썬 주피터 이런게 다 깔려있습니다. 구축이 다 됐는데... 
# 그 컴퓨터가 진짜 오래된거라 코드 하나만 돌려도 뻗어서 데드라인을 못 지킬 위험이 있기떄문에 부득이하게 윈도우에서 작업했습니다. 
# 그리고 여기에는 별도의 개발 환경 구축 없이 그냥 백준 풀 용도로 파이썬만 깔아둔 상태입니다. 따라서 이 코드 역시 정말 최소한의 모듈만 설치해서 돌아가게 만들어야 합니다. 

# 모듈 ZONE
import sqlite3 # SQLite 


def init_db():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS events (
        event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        search_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        event_type TEXT NOT NULL,
        query TEXT,
        result_count INTEGER,
        compound_id INTEGER,
        error_type TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(create_table_query)
    print('테이블이 생성되었습니다. ')
    conn.commit()
