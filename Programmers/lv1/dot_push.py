import math
def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        print("1. x = ", x)
        res_d = math.floor(math.sqrt(d*d - x*x))
        print("2. res_d = {0} / k = {1}".format(res_d, k))
        answer += (res_d // k) + 1
        print("3. answer = ", answer)
    return answer

k = 1
d = 5
print(solution(k, d))

