def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    x, y = -1, 0
    num = 1

    for i in range(n):
        print("1. (1번 for문) i = {0} / n = {1}".format(i, n))
        for j in range(i, n):
            print("2. (2번 for문) j = {0} / i = {1} / n = {2}".format(j, i, n))
            if i % 3 == 0:
                x += 1
                print("3. (if) x = ", x)
            elif i % 3 == 1:
                y += 1
                print("4. (elif) y = ", y)
            else:
                x -= 1
                print("5. (else) x = ", x)
                y -= 1
                print("6. (else) y = ", y)
            answer[x][y] = num
            print("7. answer[x][y] = ", num)
            num += 1
        print("*** result *** == ", answer)
    return sum(answer, [])

n = 6
print(solution(n))