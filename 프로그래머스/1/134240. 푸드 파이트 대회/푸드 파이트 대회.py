def solution(food):
    answer = ''
    for index, value in enumerate(food[1:], start = 1):
        for value in range(1, value//2 +1):
            answer += str(index)
    answer += '0' + answer[::-1]
    
    return answer