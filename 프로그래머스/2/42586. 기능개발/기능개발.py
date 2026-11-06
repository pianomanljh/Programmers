from collections import deque
def solution(progresses, speeds):
    day_que = deque()
    answer = []
    for i in range(len(progresses)):
        day = (100 - progresses[i])/speeds[i]
        if (day % 1) != 0:
            day = int(day+1)
        day = int(day)
        day_que.append(day)
    while day_que:
        a = day_que.popleft()
        count = 1
        while day_que and (a >= day_que[0]):
            day_que.popleft()
            count += 1
        answer.append(count)
        
    return answer