# 진짜 단순하게 생각했을때의 풀이(brute force)
# def solution(prices):
#     answer = [i for i in range(len(prices)-1,-1, -1)]
#     for i in range(len(prices)-1):
#         for j in range(i+1,len(prices)):
#             if prices[i] > prices[j]:
#                 answer[i] = j-i
#                 break
#     return answer

def solution(prices):
    answer = [i for i in range(len(prices)-1,-1, -1)]
    st = []
    for i in range(len(prices)):
        while st and prices[st[-1]] > prices[i]:
            p = st.pop()
            answer[p] = i-p
        st.append(i)
    return answer