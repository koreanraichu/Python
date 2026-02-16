# M1V1 = M2V2
# 이거 되게 간단한 희석 농도 구하는 공식입니다. 
# 예를 들어서 100mM 염화나트륨 용액 xml를 넣어서 50mM 염화나트륨 100ml를 만들어야 해요. 그러면 100 * x = 50 * 100이 되거든요. 
# 그러면 100x = 5000이니까 100으로 나누면 x = 50이 됩니다. 
# 예시를 몰(M)로 들어서 글치 스톡 솔루션(농축액)에도 적용되는 공식입니다 이거. 

# 참고로 단위 통일하셔야 합니다. 하나는 리터 하나는 밀리리터 이렇게 하시면 계산 뻑나요. 

# V1 구하는 함수
def calculate_v1 (m1, m2, v2): 
    v1 = (m2 * v2) / m1
    return v1

# V2 구하는 함수 
# 근데 이게 필요함? 
def calculate_v2 (m1, v1, m2): 
    v2 = (m1 * v1) / m2
    return v2

# M1 구하는 함수
def calculate_m1 (v1, m2, v2):
    m1 = (m2 * v2) / v1
    return m1

# M2 구하는 함수
def calculate_m2 (m1, v1, m2): 
    m2 = (m1 * v1) / v2
    return m2

# 예시(v1)
# 5x stock solution으로 2x(2배 농도) 용액 500ml를 만들 때 필요한 부피는? (보통 나머지는 물로 채웁니다)
v1 = calculate_v1(5, 2, 500)
print(f'v1: {v1:.2f}')

# 예시(v2)
# 10x stock solution 100ml을 써서 2x 용액을 몇 ml 만들 수 있나요? 
v2 = calculate_v2(10, 100, 2)
print(f'v2: {v2:.2f}')

# 예시(m1)
# 농도를 모르는 stock solution을 300ml 넣어서 2x 용액 600ml를 만들었다면 원재료의 농도는? 
m1 = calculate_m1(300, 2, 600)
print(f'm1: {m1:.2f}')

# 예시(m2)
# 5x stoxk solution 100ml을 이용하여 만들 수 있는 500ml 용액의 농도는? 
m2 = calculate_m2(5, 100, 500)
print(f'm2: {m2:.2f}')