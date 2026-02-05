# 베이즈 정리: 어떤 사건이 서로 배반하는 원인 둘에 의해 일어난다고 할 때 실제 사건이 일어났을 때 이것이 두 원인 중 하나일 확률을 구하는 정리
# 공식: P(A|B) = P(B|A) * P(A) / P(B)

# P(A): 사전확률
# P(B): 주변 우도(marginal likelihood)
# P(A|B): B의 값이 주어졌을 때 A의 사후 확률(여기서 구해야 하는 거))
# P(B|A): A가 주어졌을 때 B의 조건부 확률
# P(B|not A): A가 주어지지 않았을 때 B의 조건부 확률

# 함수 매개변수: P(A), P(B|A), P(B|not A) 순서대로 입력해주세요 
def bayes_theorem(prior, sensitivity, false_positive):
    
    # P(B)
    # P(B) = P(B|A) * P(A) + P(B|not A) * P(not A) (전확률의 정리인가 있음 아무튼)
    marginal_likelihood = (prior * sensitivity) + ((1 - prior) * false_positive) # P(B)를 계산해야 함
    
    # P(A|B)
    # P(A|B) = P(B|A) * P(A) / P(B) (위에 공식 써있음)
    posterior = (prior * sensitivity) / marginal_likelihood
    return posterior

result = bayes_theorem(0.01, 0.95, 0.05)
print(f"P(A|B): {result:.2%}")