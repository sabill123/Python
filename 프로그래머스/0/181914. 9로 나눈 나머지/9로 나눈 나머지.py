def solution(number):
    q=0
    if (int(number) > 9999):
        return int(number)%9
    answer=0
    for i in number:
        answer += int(i)
    q = int(answer)%9
    return q