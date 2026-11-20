from collections import deque
def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    que = deque()
    visit = [[0] * m for _ in range(n)]
    que.append([n, m])
    visit[n-1][m-1] = 1
    
    while que:
        q = que.popleft()
        i = q[0]
        j = q[1]
        if i == 1 and j== 1:
            answer = visit[i-1][j-1]
            break
        if i-1 > 0 and maps[i-2][j-1] and visit[i-2][j-1] == 0:
            que.append([i-1,j])
            visit[i-2][j-1] = visit[i-1][j-1] + 1
        if 0 < j-1 and maps[i-1][j-2] and visit[i-1][j-2] == 0:
            que.append([i,j-1])
            visit[i-1][j-2] = visit[i-1][j-1] + 1
        if i+1 <= n and maps[i][j-1] and visit[i][j-1] == 0:
            que.append([i+1,j])
            visit[i][j-1] = visit[i-1][j-1] + 1
        if j+1 <= m and maps[i-1][j] and visit[i-1][j] == 0:
            que.append([i,j+1])
            visit[i-1][j] = visit[i-1][j-1] + 1

    return answer
