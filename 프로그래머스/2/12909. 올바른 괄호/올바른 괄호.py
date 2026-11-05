def solution(s):
    lst = []
    if s[0] == ')' :
        return False
    for i in range(len(s)):
        if s[i] == '(' :
            lst.append(s[i])
        else:
            if not lst:
                return False
            lst.pop()
    if lst:
        return False
    return True