def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)
        print("1. k = ", k)
        for j in range(2, int(i**0.5) + 1):
            print("2. j = ", j)
            if i % j == 0 and i//j <= 10000000:
                k = i//j
                print("3. k({2}) = i({0}) // j({1})".format(i, j, k))
                break
        answer.append(k)
        print("4. answer = ", answer)
    return answer

begin = 1
end = 10
print(solution(begin, end))