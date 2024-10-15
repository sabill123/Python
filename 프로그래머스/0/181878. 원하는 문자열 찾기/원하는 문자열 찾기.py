def solution(myString, pat):
    string = myString.lower()
    pat_1 = pat.lower()
    if pat_1 in string:
        return 1
    else: return 0
