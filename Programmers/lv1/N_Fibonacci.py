import sys
def memoization_Fibo(n):
    memo = [1, 1]

    if n < 2:
        return memo[n]

    for i in range(2, n+1):
        memo[i] = memo[i-2] + memo[1-1]

    return memo[n]

n = 6
print(memoization_Fibo(n))