def solution(word):
    answer = 0
    lst = ['A','E','I','O','U']
    dic = dict()
    for idx, c in enumerate(lst):
        dic[c] = idx
        
    for i, a in enumerate(word):
        sum = ((5**(5-i))-1)//4
        answer += sum*dic[a] + 1
        
    return answer