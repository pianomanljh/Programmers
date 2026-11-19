def dfs(numbers, target, number, idx):
    global result
    result += number
    if idx+1 == len(numbers):
        if target == result:
            global answer
            answer += 1
        return 0
    dfs(numbers, target, numbers[idx+1], idx+1)
    result -= numbers[idx+1]
    dfs(numbers, target, -numbers[idx+1], idx+1)
    result += numbers[idx+1]

def solution(numbers, target):
    global answer
    answer = 0
    global result
    result = 0
    dfs(numbers, target, numbers[0], 0)
    result -= numbers[0]
    dfs(numbers, target, -numbers[0], 0)
    result += numbers[0]
    return answer