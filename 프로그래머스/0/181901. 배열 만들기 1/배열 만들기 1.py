def solution(n, k):
    answer = []
    num = n
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
    answer.sort()
    return answer