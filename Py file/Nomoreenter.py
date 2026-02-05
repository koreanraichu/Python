import re
import tkinter as tk
from tkinter import filedialog
import os

def format_dialogue(text):
    """
    다양한 따옴표 쌍 사이의 빈 줄 제거
    """
    # 개행 정리 (Windows → Unix)
    text = text.replace('\r\n', '\n')

    # 다양한 따옴표 조합 처리
    patterns = [
        # 유니코드 큰따옴표: “ ”
        (r'(“[^”]*?”)\s*\n\s*\n\s*(“[^”]*?”)', r'\1\n\2'),
        # 유니코드 작은따옴표: ‘ ’
        (r'(‘[^’]*?’)\s*\n\s*\n\s*(‘[^’]*?’)', r'\1\n\2'),
        # ASCII 큰따옴표: " "
        (r'("[^"]*?")\s*\n\s*\n\s*("[^"]*?")', r'\1\n\2'),
        # ASCII 작은따옴표: ' '
        (r"('[^']*?')\s*\n\s*\n\s*('[^']*?')", r'\1\n\2'),
    ]

    prev_text = None
    while text != prev_text:
        prev_text = text
        for pattern, repl in patterns:
            text = re.sub(pattern, repl, text, flags=re.DOTALL)

    return text

def select_file():
    """
    파일 선택 다이얼로그를 열어서 파일 경로를 반환
    """
    # tkinter 창이 보이지 않도록 설정
    root = tk.Tk()
    root.withdraw()
    
    # 파일 선택 다이얼로그
    file_path = filedialog.askopenfilename(
        title="변환할 텍스트 파일 선택",
        filetypes=[
            ("텍스트 파일", "*.txt"),
            ("모든 파일", "*.*")
        ],
        initialdir=os.path.expanduser("~/Desktop")  # 바탕화면을 기본 경로로
    )
    
    root.destroy()
    return file_path

def select_save_location(default_name):
    """
    저장 위치 선택 다이얼로그
    """
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.asksaveasfilename(
        title="변환된 파일 저장 위치",
        defaultextension=".txt",
        filetypes=[
            ("텍스트 파일", "*.txt"),
            ("모든 파일", "*.*")
        ],
        initialdir=os.path.expanduser("~/Desktop"),
        initialfile=default_name
    )
    
    root.destroy()
    return file_path

def process_file(input_file=None, output_file=None):
    """
    파일을 읽어서 변환 후 저장하는 함수
    """
    try:
        # 파일 읽기 (UTF-8 인코딩)
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("[디버그] 원본 내용 ==========")
        print(content)

        formatted_content = format_dialogue(content)

        print("[디버그] 변환된 내용 ==========")
        print(formatted_content)
        
        # 출력 파일명 설정
        if output_file is None:
            if input_file.endswith('.txt'):
                output_file = input_file.replace('.txt', '_formatted.txt')
            else:
                output_file = input_file + '_formatted'
        
        # 변환된 내용 저장
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        
        print(f"변환 완료: {output_file}")
        
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {input_file}")
    except Exception as e:
        print(f"오류 발생: {e}")

def process_with_gui():
    print("파일을 선택해주세요...")
    input_file = select_file()
    print(f"[디버그] 선택된 input 파일 경로: {input_file}")

    if not input_file:
        print("파일이 선택되지 않았습니다.")
        return

    default_output = os.path.basename(input_file).replace('.txt', '_formatted.txt')
    output_file = select_save_location(default_output)
    print(f"[디버그] 선택된 output 파일 경로: {output_file}")

    if not output_file:
        print("저장 경로가 선택되지 않았습니다.")
        return

    process_file(input_file, output_file)


# 사용 예시
if __name__ == "__main__":
    # 테스트용 텍스트
    sample_text = '''문단입니다.

"첫 번째 대화"

"두 번째 대화"

"세 번째 대화"

문단입니다.

"네 번째 대화"

"다섯 번째 대화"

-효과음

"여섯 번째 대화"

문단입니다.'''

    print("=== 변환 전 ===")
    print(sample_text)
    print("\n=== 변환 후 ===")
    print(format_dialogue(sample_text))
    
    print("\n" + "="*50)
    print("사용법:")
    print("1. GUI로 파일 선택: process_with_gui()")
    print("2. 경로 직접 입력: process_file('input.txt')")
    print("3. 경로 + 출력파일 지정: process_file('input.txt', 'output.txt')")
    print("4. 파일 선택만: process_file()  # 다이얼로그가 열립니다")

process_with_gui()
