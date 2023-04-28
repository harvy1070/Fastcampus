def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        print(s[-4:])
        if s[-4:] == [1,2,3,1]:
            cnt += 1
            for _ in range(4):
                s.pop()
    return cnt

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))