def solution(my_string, n):
    answer = ''
    m = len(my_string)
    answer = my_string[((m-n)):]
    return answer