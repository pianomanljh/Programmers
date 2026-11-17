from collections import deque
visit = []
def dfs(n, wires, i, cnt):
    cnt += 1
    for j in range(n):
        if ([i+1,j+1] in wires or [j+1,i+1] in wires) and not visit[j]:
            visit[j] = 1
            cnt = dfs(n, wires, j, cnt)
    return cnt
def solution(n, wires):
    answer = -1
    global visit
    wires = deque(wires)
    for i in range(len(wires)):
        visit = [0]*n
        visit[0] = 1
        temp = wires.popleft()
        k = dfs(n,wires,0, 0)
        wires.append(temp)
        ab = abs(n-2*k)
        if answer == -1 or ab < answer:
            answer = ab
    return answer