def solution(prices):
    answer = [i for i in range(len(prices)-1,-1, -1)]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j-i
                break
    return answer