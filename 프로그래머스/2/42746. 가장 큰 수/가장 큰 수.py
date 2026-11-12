def solution(numbers):
    answer = ''
    numbers_str = [str(n) for n in numbers]
    numbers_str.sort(key = lambda x: x*3)
    for i in range(len(numbers_str)-1, -1, -1):
        answer += numbers_str[i]
    return "0" if answer[0] == "0" else answer