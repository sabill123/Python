def solution(my_string):
    result = [0] * 52  # A-Z와 a-z에 해당하는 52개의 자리
    for char in my_string:
        if 'A' <= char <= 'Z':  # 대문자
            result[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':  # 소문자
            result[ord(char) - ord('a') + 26] += 1
    return result
