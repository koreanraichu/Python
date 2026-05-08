from db import init_db
from generator import EventGenerator
from analysis import run_analysis

def run_all():
    # 1. DB 생성
    init_db()

    # 2. 데이터 생성
    gen = EventGenerator()
    for _ in range(1000):
        gen.generate_search_flow()

    # 3. 분석 실행
    run_analysis()


def main():
    run_all()


if __name__ == "__main__":
    main()