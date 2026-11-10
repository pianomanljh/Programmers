def solution(clothes):
    s = dict()
    answer = 1
    for item in clothes:
        s[item[1]] = s.get(item[1],0) + 1
    for key in s:
        answer *= s[key] + 1
    return answer-1