def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def solution(n, k):
    result = []
    num_list = [i for i in range(1, n+1)]
    #print("1. num_list = ", num_list)
    while(n!=0):
        num_case = factorial(n - 1)
        print("1. num_case = ", num_case)
        idx = k // num_case
        print("2. idx(k // num_case) = ", idx)
        k = k % num_case
        print("3. k(k%num_case) = ", k)
        print("***** num_list = {0} *****".format(num_list))
        if k == 0:
            result.append(num_list.pop(idx - 1))
            print("4. <if> result = ", result)
        else:
            result.append(num_list.pop(idx))
            print("5. <else> result = ", result)

        n -= 1
        print("6. n = ", n)
    return result

n = 3
k = 5
print(solution(n, k))