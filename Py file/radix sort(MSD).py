# 얘는 MSD라고 해서 앞자리부터 보는거예요. 왜죠? 아 이게요...
# 예를 들어보겠습니다. 1부터 10까지 들어있는 배열인데 내용물이 문자야... 이거 LSD로 하면 1, 10, 2, 3, 4, 5, 6, 7, 8, 9가 됩니다.
# 아니 왜 1 다음에 10이 옴? 이거 뭥미? 그래서 이럴때는 MSD를 도입해서 10의 자리부터 보는겁니다. 이렇게 하면 10의 자리가 1인 10이 뒤로 가거든요.
# 코드: 제미나이


def msd_radix_sort(arr, index=0):
    # 원소가 1개 이하면 정렬 완료
    if len(arr) <= 1:
        return arr

    # ASCII 코드 기준 버킷 (0~255) + 현재 index에서 문자열이 끝난 경우를 담을 버킷
    done = []
    buckets = [[] for _ in range(256)]

    for s in arr:
        if index >= len(s):
            # 현재 자릿수보다 짧은 문자열은 가장 먼저 배치
            done.append(s)
        else:
            buckets[ord(s[index])].append(s)

    # 각 버킷 내부를 다음 글자(index + 1) 기준으로 재귀 정렬
    result = done
    for bucket in buckets:
        if bucket:
            result.extend(msd_radix_sort(bucket, index + 1))
    print(result)

    return result


# 실행 예시
# 아 뭔데 이거 왜 길어진건데 이러면 나 못알아본다고...
words = [
    "banana",
    "apple",
    "app",
    "care",
    "dad",
    "alloy",
    "band",
    "date",
    "dare",
    "cat",
    "bad",
]
print(msd_radix_sort(words))
