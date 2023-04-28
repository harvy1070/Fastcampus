def solution(s):
    arr = list(map(int, s.split(' ')))
    arr.sort()
    return str(arr[0]) + " " + str(arr[-1])

s = "1 2 3 4"
print(solution(s))