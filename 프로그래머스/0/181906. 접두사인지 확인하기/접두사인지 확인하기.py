def solution(my_string, is_prefix):
    answer = 0
    result = []
    for i in range(len(my_string)):
        result.append(my_string[:i])
    result.sort()
    if is_prefix in result:
        answer = 1
    return answer