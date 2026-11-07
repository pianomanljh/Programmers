def solution(priorities, location):
    count = 0
    while True:
        max_index = priorities.index(max(priorities))
        for _ in range(max_index):
            priorities.append(priorities.pop(0))
        if location - count >= max_index:
            location -= max_index
        else:
            location = location - max_index + len(priorities)
        count += 1
        if (count -1) == location:
            return location + 1
        priorities.pop(0)