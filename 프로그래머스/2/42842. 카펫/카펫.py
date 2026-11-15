def solution(brown, yellow):
    n = brown + yellow
    for i in range(1,n//2 + 1):
        if n % i == 0 and (i + n//i)*2-4 == brown:
            return [n//i, i]
