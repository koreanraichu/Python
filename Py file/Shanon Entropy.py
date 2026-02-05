# 자세한 설명은... 내 조만간 블로그에 올리리다... 
# 정보 엔트로피라고 하면 뭔지 아는 분들도 계십니다. 
import math
from collections import Counter

def calculate_shannon_entropy(data):
    # 1. 데이터 내 각 요소의 빈도 계산
    counts = Counter(data)
    total_count = len(data)
    
    # 2. 확률 계산 및 엔트로피 합산
    entropy = 0
    for count in counts.values():
        p_x = count / total_count
        # p_x가 0일 때 log(0)은 정의되지 않으므로 조건문 처리
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)
            
    return entropy

# 예시 데이터
data = [1, 1, 2, 2, 3, 3, 3, 3]
print(f"Shannon Entropy: {calculate_shannon_entropy(data):.4f}")
