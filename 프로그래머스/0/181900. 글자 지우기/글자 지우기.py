def solution(my_string, indices):
    # 문자열을 리스트로 변환
    my_string = list(my_string)
    
    # 주어진 인덱스를 기준으로 삭제 (인덱스를 역순으로 정렬해야 오류를 방지 가능)
    for i in sorted(indices, reverse=True):
        del my_string[i]

    # 리스트를 다시 문자열로 변환하여 반환
    return ''.join(my_string)
