# 첫 풀이
# def dfs(numbers, target, number, idx):
#     global result
#     result += number
#     if idx+1 == len(numbers):
#         if target == result:
#             global answer
#             answer += 1
#         return 0
#     dfs(numbers, target, numbers[idx+1], idx+1)
#     result -= numbers[idx+1]
#     dfs(numbers, target, -numbers[idx+1], idx+1)
#     result += numbers[idx+1]

# def solution(numbers, target):
#     global answer
#     answer = 0
#     global result
#     result = 0
#     dfs(numbers, target, numbers[0], 0)
#     result -= numbers[0]
#     dfs(numbers, target, -numbers[0], 0)
#     result += numbers[0]
#     return answer

# 개선 풀이
def solution(numbers, target):
    def dfs(idx, current_sum):
        if idx == len(numbers):
            return 1 if current_sum == target else 0
        
        return (
            dfs(idx + 1, current_sum + numbers[idx])
            + dfs(idx + 1, current_sum - numbers[idx])
        )

    return dfs(0, 0)