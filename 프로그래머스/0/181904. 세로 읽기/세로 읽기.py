def solution(my_string, m, c):
    answer = ''
    c = c - 1
    for i in range(len(my_string) // m):
        answer += my_string[c + (m * i)]
    return answer
