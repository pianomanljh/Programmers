# 첫 풀이
# def solution(priorities, location):
#     count = 0
#     while True:
#         max_index = priorities.index(max(priorities))
#         for _ in range(max_index):
#             priorities.append(priorities.pop(0))
#         if location - count >= max_index:
#             location -= max_index
#         else:
#             location = location - max_index + len(priorities)
#         count += 1
#         if (count -1) == location:
#             return location + 1
#         priorities.pop(0)

# 최적화
from collections import deque

def solution(priorities, location):
    # (우선순위, 초기 인덱스) 쌍으로 덱 구성
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0

    while queue:
        cur = queue.popleft()
        # 현재 문서보다 우선순위가 높은 문서가 남아있는지 확인
        if any(cur[0] < item[0] for item in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer