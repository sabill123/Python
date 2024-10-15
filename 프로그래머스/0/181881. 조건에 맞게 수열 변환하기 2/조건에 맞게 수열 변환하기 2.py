def solution(arr):
    count = 0  # 변화가 발생한 반복 횟수를 기록
    while True:
        prev_arr = arr[:]  # 현재 배열을 복사하여 저장
        arr = []
        
        for i in prev_arr:
            if i >= 50 and i % 2 == 0:
                arr.append(i / 2)
            elif i < 50 and i % 2 == 1:
                arr.append((i * 2) + 1)
            else:
                arr.append(i)
        
        count += 1  # 반복 횟수 증가

        # 변화가 없다면 반복 종료
        if arr == prev_arr:
            return count - 1  # 마지막으로 변하지 않은 시점의 횟수를 반환
