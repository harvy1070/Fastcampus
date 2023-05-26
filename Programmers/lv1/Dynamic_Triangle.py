def solution(triangle):
    answer = 0
    print(triangle[1][1])
    for i in range(1, len(triangle)):
        #print(triangle[i])
        for j in range(len(triangle[i])):
            print(triangle)
            #print("1. i = {0}, j = {1}, triangle[{0}] -> {2}".format(i, j, triangle[i]))
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
                #print("<j == 0> : triangle[{0}][{1}] >>> {2}".format(i, j, triangle[i][j]))
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
                #print("<j == len(triangle[{0}]) - 1> : triangle[{0}][{1}] >>> {2}".format(i, j, triangle[i-1][j-1]))
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                #print("<else> : triangle[{0}][{1}] += max(triangle[{0}-1][{1}-1], triangle[{0}-1][j]) >>> {2}".format(i, j, triangle[i][j]))
    answer = max(triangle[-1])
    print(triangle[-1])
    #print("************ result = {0} ************".format(answer))
    return answer

triangle = 	[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))