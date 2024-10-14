def solution(num_list):
    odd = 0
    for i in range(0, len(num_list), 2):
        odd += num_list[i]
    pair = 0 
    for i in range(1, len(num_list), 2):
        pair += num_list[i]
    if odd > pair:
        return odd
    else: return pair
