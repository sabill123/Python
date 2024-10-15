def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            if i % 2 == 0:
                i = i // 2  # 짝수일 때는 2로 나눔
            else:
                i = (i - 1) // 2  # 홀수일 때는 1을 뺀 후 2로 나눔
            answer += 1  # 연산 횟수를 누적
    return answer
