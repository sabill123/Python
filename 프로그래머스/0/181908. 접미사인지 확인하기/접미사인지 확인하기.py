def solution(my_string, is_suffix):
    answer = 0
    result = []
    for i in range(len(my_string)):
        result.append(my_string[i:])
    result.sort()
    
    if is_suffix in result:
        answer = 1
    return answer