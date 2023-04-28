def solution(columns, rows, queries):
    answer = []
    matrix = [[0 for i in range(columns + 1)] for j in range(rows + 1)]
    num = 1
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            matrix[row][column] = num
            #print("1. matrix[{0}][{1}] = {2}".format(row, column, num))
            num += 1
    for x1, y1, x2, y2 in queries:
        print("2. x1:{0} / y1:{1} / x2:{2} / y2:{3}".format(x1, y1, x2, y2))
        tmp = matrix[x1][y1]
        print("3. tmp = ", tmp)
        mini = tmp
        print("4. mini = ", mini)
        for k in range(x1, x2):
            test = matrix[k+1][y1]
            print("<x1:{0} / x2:{1}> test = {2}".format(x1, x2, test))
            print("<x1:{0} / x2:{1}> k = {2}".format(x1, x2, k))
            matrix[k][y1] = test
            mini = min(mini, test)
        for k in range(y1, y2):
            test = matrix[x2][k+1]
            print("<y1:{0} / y2:{1}> test = {2}".format(y1, y2, test))
            print("<y1:{0} / y2:{1}> k = {2}".format(y1, y2, k))
            matrix[x2][k] = test
            mini = min(mini, test)
        for k in range(x2, x1, -1):
            test = matrix[k-1][y2]
            print("<x2:{0} / x1:{1}> test = {2}".format(x2, x1, test))
            print("<x2:{0} / x1:{1}> k = {2}".format(x2, x1, k))
            matrix[k][y2] = test
            mini = min(mini, test)
        for k in range(y2, y1, -1):
            test = matrix[x1][k-1]
            print("<y2:{0} / y1:{1}> test = {2}".format(y2, y1, test))
            print("<y2:{0} / y1:{1}> k = {2}".format(y2, y1, k))
            matrix[x1][k] = test
            mini = min(mini, test)

        matrix[x1][y1+1] = tmp
        print("<result> matrix[{0}][{1}] = {2}".format(x1, y1+1, tmp))
        answer.append(mini)
        print("*** answer = ", answer)
    return answer

cc = 6
rr = 6
qq = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(cc, rr, qq))
