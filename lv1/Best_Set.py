def solution(n, s):
    if n > s:
        return -1
    result = []

    initial = s // n
    print("1. initial = {0}".format(s//n))
    for _ in range(n):
        result.append(initial)
        print("2. result = {0}, initial = {1}".format(result, initial))
    idx = len(result) - 1
    print("3. idx = {0}".format(idx))

    for _ in range(s % n):
        print("********** result === {0} **********".format(result))
        result[idx] += 1
        print("4. result[{0}] = {1}".format(idx, result[idx]))
        idx -= 1
        print("5. idx = {0}".format(idx))
    return result

n, s = 2, 9
print(solution(n, s))