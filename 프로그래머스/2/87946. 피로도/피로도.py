from itertools import permutations
def solution(k, dungeons):
    lst = list(permutations(dungeons))
    result = 0
    for d in lst:
        count = 0
        c_k = k
        for cur in d:
            if c_k < cur[0]:
                if result < count:
                    result = count
                break
            count += 1
            c_k -= cur[1]
        if len(dungeons) == count:
            return count
    return result