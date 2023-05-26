from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    q, q1, q2 = deque(goal), deque(cards1), deque(cards2)
    b, c = q1.popleft(), q2.popleft()
    while q:
        a = q.popleft()
        print(a)
        if a == b:
            if len(q1) > 0:
                b = q1.popleft()
                print(b)
        elif a == c:
            if len(q2) > 0:
                c = q2.popleft()
                print(c)
        else:
            return 'No'
    return 'Yes'

cards1 = ["WANT", "TO"]
cards2 = ["I", "DRINK", "WATER"]
goal = ["I", "WANT", "TO", "DRINK", "WATER"]
print(solution(cards1, cards2, goal))