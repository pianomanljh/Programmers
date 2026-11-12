# 내 풀이
def solution(numbers):
    answer = ''
    numbers_str = [str(n) for n in numbers]
    numbers_str.sort(key = lambda x: x*3)
    for i in range(len(numbers_str)-1, -1, -1):
        answer += numbers_str[i]
    return "0" if answer[0] == "0" else answer

# 간결풀이
# def solution(numbers):
#     numbers_str = [str(n) for n in numbers]
#     numbers_str.sort(key=lambda x: x * 3, reverse=True)
#     answer = "".join(numbers_str)
#     return "0" if answer[0] == "0" else answer

# 정석 문제 풀이
# from functools import cmp_to_key

# def compare(a, b):
#     # a를 앞에 두었을 때(a + b)가 더 크면 순서를 유지(-1), 작으면 바꿈(1)
#     if a + b > b + a:
#         return -1
#     elif a + b < b + a:
#         return 1
#     else:
#         return 0

# def solution(numbers):
#     numbers_str = list(map(str, numbers))
#     numbers_str.sort(key=cmp_to_key(compare))
#     answer = "".join(numbers_str)
#     return "0" if answer[0] == "0" else answer