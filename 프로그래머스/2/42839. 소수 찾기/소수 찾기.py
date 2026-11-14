from collections import deque
def is_prime(n):
    if n<= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    lst = deque([(s, {i}) for i,s in enumerate(list(numbers))])

    n = len(numbers)
    while lst:
        num = lst.popleft()
        if is_prime(int(num[0])):
                answer.append(int(num[0]))
        for i in range(len(numbers)):
            if i not in num[1]:
                lst.append((num[0] + numbers[i], num[1] | {i}))
    return len(set(answer))