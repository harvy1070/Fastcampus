from math import ceil
def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1
    print("1. W = ", W)
    start = 1

    for s in stations:
        answer += max(ceil((s-w-start)/W), 0)
        print("2. max(ceil(({0}-{1}-{2}) / {3}), 0)".format(s, w, start, W))
        print(">>> answer = {0}".format(answer))
        start = s + w + 1
        print("3. start = {0} + {1} + 1 >> {2}".format(s, w, start))

    if n >= start:
        print("4. {0} >= {1}".format(n, start))
        answer += ceil((n - start + 1) / W)
        print("5. ceil(({0} - {1} + 1) / {2})".format(n, start, W))
        print(">>> answer = {0}".format(answer))

    return answer

n, w = 16, 2
stations = [9]
print(solution(n, stations, w))
