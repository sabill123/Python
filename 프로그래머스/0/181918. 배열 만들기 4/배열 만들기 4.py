def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        # 스택이 비어 있으면 현재 요소를 추가
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            # 스택의 마지막 요소가 현재 요소보다 작으면 현재 요소를 추가
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            # 스택의 마지막 요소가 현재 요소보다 크거나 같으면, 그 요소를 제거
            elif stk[-1] >= arr[i]:
                stk.pop()
                # 제거 후 스택이 비어 있다면 새 요소 추가
                if not stk or stk[-1] < arr[i]:
                    stk.append(arr[i])
                    i += 1
    return stk
