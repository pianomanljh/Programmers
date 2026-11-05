# [풀이 1] 초기 작성 풀이 (스택 활용)
# def solution(s):
#     lst = []
#     if s[0] == ')' :
#         return False
#     for i in range(len(s)):
#         if s[i] == '(' :
#             lst.append(s[i])
#         else:
#             if not lst:
#                 return False
#             lst.pop()
#     if lst:
#         return False
#     return True

# [풀이 2] 리팩터링 풀이 (스택 최적화)
def solution(s):
    lst = []
    for c in s:
        if c == '(' :
            lst.append(c)
        else:
            if not lst:
                return False
            lst.pop()
    
    return not lst

# [풀이 3] 추가 개선안 (카운터 O(1) 공간 복잡도)
# def solution(s):
#     count = 0
#     for char in s:
#         count += 1 if char == '(' else -1
#         if count < 0: return False
#     return count == 0