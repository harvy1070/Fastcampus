def solution(arr):
    result = [0, 0]
    length = len(arr)
    def compression(a, b, l):
        start = arr[a][b]
        for i in range(a, a+l):
            for j in range(b, b+l):
                print("arr[{0}][{1}] = {2}".format(i, j, arr[i][j]))
                if arr[i][j] != start:
                    print("start = ", start)
                    print(l)
                    l = l // 2
                    compression(a, b, l)
                    #print("comp1 = ", compression)
                    compression(a, b+l, l)
                    #print("comp2 = ", compression)
                    compression(a+l, b, l)
                    #print("comp3 = ", compression)
                    compression(a+l, b+l, l)
                    #print("comp4 = ", compression)
                    return
        result[start] += 1
    compression(0, 0, length)
    return (result)

arr = [[1, 1, 1, 1, 1, 1, 1, 1],\
       [0, 1, 1, 1, 1, 1, 1, 1],\
       [0, 0, 0, 0, 1, 1, 1, 1],\
       [0, 1, 0, 0, 1, 1, 1, 1],\
       [0, 0, 0, 0, 0, 0, 1, 1],\
       [0, 0, 0, 0, 0, 0, 0, 1],\
       [0, 0, 0, 0, 1, 0, 0, 1],\
       [0, 0, 0, 0, 1, 1, 1, 1]]

print(solution(arr))