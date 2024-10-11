def solution(answers):
    # 각 수포자의 답안 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 각 수포자가 맞힌 개수를 저장할 리스트
    scores = [0, 0, 0]
    
    # 정답과 각 수포자의 패턴을 비교
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    # 가장 높은 점수를 찾고, 그 점수를 가진 수포자 찾기
    max_score = max(scores)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return result