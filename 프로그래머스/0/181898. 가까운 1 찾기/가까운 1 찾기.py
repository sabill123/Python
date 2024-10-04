def solution(arr, idx):
    # idx부터 끝까지 탐색
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i  # 1을 찾으면 해당 인덱스 반환
    
    return -1  # 1을 찾지 못하면 -1 반환
