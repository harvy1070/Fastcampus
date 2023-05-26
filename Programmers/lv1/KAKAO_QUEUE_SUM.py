from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4

    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1 + tot2

    if total % 2 != 0:
        return -1

    while True:
        if tot1 > tot2:
            target = queue1.popleft()
            print("<if> 1. target = ", target)
            queue2.append(target)
            print("<if> 2. queue2 = ", queue2)
            tot1 -= target
            print("<if> 3. tot1 = ", tot1)
            tot2 += target
            print("<if> 4. tot2 = ", tot2)
            answer += 1
        elif tot1 < tot2:
            target = queue2.popleft()
            print("<elif> 1. targat = ", target)
            queue1.append(target)
            print("<elif> 2. queue1 = ", queue1)
            tot1 += target
            print("<elif> 3. tot1 = ", tot1)
            tot2 -= target
            print("<elif> 4. tot2 = ", tot2)
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2))