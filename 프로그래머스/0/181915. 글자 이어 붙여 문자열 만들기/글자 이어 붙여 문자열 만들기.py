def solution(my_string, index_list):
    answer = []
    for i in range(len(index_list)):
        answer.append(my_string[index_list[i]])
    answer2 = ''.join(answer)
    return answer2