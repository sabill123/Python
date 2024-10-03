def solution(q, r, code):
    answer = ''
    result = []
    
    # 인덱스 i가 (i % q == r)를 만족하는 경우 result에 추가
    for i in range(len(code)):
        if i % q == r:
            result.append(i)
    
    # result에 저장된 인덱스를 이용해 code에서 문자를 추출
    for index in result:
        answer += code[index]
    
    return answer
