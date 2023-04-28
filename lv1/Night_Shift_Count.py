# 효율성 테스트 통과 안됨
def solution(n, works):
    if n >= sum(works):
        return 0

    works.sort()
    for _ in range(n):
        works[-1] -= 1
        works.sort()

    return sum([w**2 for w in works])

import heapq
def solution2(n, works):
    if n >= sum(works):
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        print("1. i = ", i)
        i += 1
        print("2. i += 1 >> {0}".format(i))
        heapq.heappush(works, i)
    return sum([w ** 2 for w in works])

def solution3(n, works):
    answer = 0
    heap = []

    for work in works:
        #print("1. work = {0}, -work = {1}".format(work, -work))
        heapq.heappush(heap, (-work, work))
        print("1. heap = {0}".format(heap))

    while True:
        if n == 0:
            break
        work = heapq.heappop(heap)[1] - 1
        print("2. work = {0}".format(work))
        heapq.heappush(heap, (-work, work))
        print("3. heap = {0}, -work = {1}, work = {2}".format(heap, -work, work))
        n -= 1
        print("4. n = {0}".format(n))

    for h in heap:
        print("5. h = {0}".format(h))
        if h[1] < 0:
            continue
        answer += h[1] * 2
        print("6. answer = {0}".format(answer))
    return answer

works = [4, 3, 3]
n = 4
print(solution3(n, works))