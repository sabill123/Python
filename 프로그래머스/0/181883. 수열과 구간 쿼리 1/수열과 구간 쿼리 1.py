def solution(arr, queries):
    for i in range(0, len(queries)):
        for x in range(queries[i][0], queries[i][1]+1):
            arr[x] += 1
    return arr