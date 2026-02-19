import numpy as np
import matplotlib.pyplot as plt # 시각화는 옵션입니다


def visualize_pi(n):
    # 0~1 사이의 난수 n개 생성
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    # 원점과의 거리 계산
    distance = x ** 2 + y ** 2

    # 원 안과 밖 구분
    inside = distance <= 1
    outside = ~inside

    # 파이 추정치 계산
    pi_estimate = 4 * np.sum(inside) / n

    # 그래프 그리기
    plt.figure(figsize=(8, 8))

    # 원 안의 점 (빨간색)
    plt.scatter(x[inside], y[inside], s=1, color='red', alpha=0.5, label='Inside Circle')
    # 원 밖의 점 (파란색)
    plt.scatter(x[outside], y[outside], s=1, color='blue', alpha=0.5, label='Outside Circle')

    # 4분원 테두리 그리기
    theta = np.linspace(0, np.pi / 2, 100)
    plt.plot(np.cos(theta), np.sin(theta), color='black', linewidth=2)

    # 그래프 설정
    plt.title(f'Monte Carlo Pi Estimation (n={n})\nEstimated Pi: {pi_estimate}', fontsize=15)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right', markerscale=10)
    plt.axis('equal')
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()


# 시각화를 위해 점의 개수를 10,000개 정도로 설정 (너무 많으면 렌더링이 느려집니다)
visualize_pi(100000)