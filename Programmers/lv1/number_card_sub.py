from math import gcd
def get_gcd(arr):
    # list 내 최대공약수 구하기
    g = arr[0]
    print("<get_gcd> arr = {0} / arr[0] = {1}".format(arr, g))
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
        print("<get_gcd> g = {0} / arr[{1}] = {2}".format(g, i, arr[i]))
    return g

def solution(arrayA, arrayB):
    # 1, 2 조건 둘다 아닐 때
    res = 0

    # 최대 공약수 가져오기
    A, B = get_gcd(arrayA), get_gcd(arrayB)
    print("<solution> A = {0} / B = {1}".format(A, B))

    # 첫번째 조건
    for i in arrayB:
        if i % A == 0:
            break
    else:
        res = max(A, res)
    print("res1 = {0}".format(res))
    # 두번째 조건
    for i in arrayA:
        if i % B == 0:
            break
    else:
        res = max(B, res)
    print("res2 = {0}".format(res))

    return res

arrayA = [14, 35, 119]
arrayB = [18, 30, 102]

print(solution(arrayA, arrayB))