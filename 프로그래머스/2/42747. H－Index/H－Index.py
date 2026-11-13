def solution(citations):
    citations.sort(reverse = True)
    i = 0
    n = len(citations)
    while i < n and citations[i] >= i+1:
        i += 1
    return i