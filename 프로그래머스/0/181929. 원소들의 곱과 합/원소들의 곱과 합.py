import math #math를 임포트하면 math 관련 함수를 쓸수있음.

def solution(num_list):
    answer = 0 #초기화
    res1 = 1 #초기화
    res2 = 0 #초기화
        
    for i in range(len(num_list)) : #반복시작 num_list배열의 길이만큼
        res1 *= num_list[i] # 값누적(곱)
        res2 += num_list[i] # 값누적 (덧)
    res2 = (math.pow(res2, 2)) # res2 최종 제곱값
     
    if(res1 < res2): #값비교
        answer = 1 #답안 변수
  
    return answer #반환