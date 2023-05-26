import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        print("<while> 1. i = {0} / len(jobs) = {1}".format(i, len(jobs)))
        for j in jobs:
            print("<while/for> 2. j = {0}".format(j))
            if start < j[0] <= now:
                print("<while/for/if> 3-1. start:{0} < j[0]:{1} <= now:{2}".format(start, j[0], now))
                heapq.heappush(heap, [j[1], j[0]])
                print("<while/for/if> 3-2. heap = {0}".format(heap))
        if len(heap) > 0:
            print("<while/if> 4-1. len(heap):{0} > 0".format(len(heap)))
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
            print("<while/if> 4-1. current:{0} / start:{1} / now:{2} / answer:{3} / i:{4}".format(current, start, now, answer, i))
        else:
            now += 1
            print("<while/else> 4-2. now = {0}".format(now))
    return int(answer / len(jobs))

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))