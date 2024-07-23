def solution(num_list):
    num = len(num_list)
    if (num_list[num-1]>num_list[num-2]):
        num_list.append(num_list[num-1]-num_list[num-2])
    else: num_list.append(num_list[num-1]*2)
    return num_list