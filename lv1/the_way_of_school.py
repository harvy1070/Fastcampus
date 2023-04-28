def solution(m, n, puddles):
    answer = [[0] * (m+1) for i in range(n+1)]
    print("1. answer = {0}".format(answer))
    answer[1][1] = 1
    print("2. answer[1][1] = 1 = {0}".format(answer))
    for i in range(1, n+1):
        for j in range(1, m+1):
            print("3. i = {0}, j = {1}".format(i, j))
            if i == 1 and j == 1:
                print("4-1. i == 1 and j == 1 >>> pass")
                continue
            if [j, i] in puddles:
                answer[i][j] = 0
                print("4-2. answer[{0}][{1}] = 0".format(i, j))
            else:
                answer[i][j] = answer[i-1][j] + answer[i][j-1]
                print("4-3. answer[{0}][{1}] = {2}".format(i, j, answer[i][j]))
    print("************ result = {0} ************".format(answer[n][m]))
    return answer[n][m] % 1000000007


m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
