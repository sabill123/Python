def solution(my_string, queries):
    # 문자열을 리스트로 변환 (문자열은 불변이므로 리스트로 처리)
    answer = list(my_string)
    
    # 각 쿼리에 대해 처리
    for s, e in queries:
        # 부분 문자열을 뒤집어 할당
        answer[s:e+1] = answer[s:e+1][::-1]
    
    # 리스트를 문자열로 다시 변환하여 반환
    return ''.join(answer)