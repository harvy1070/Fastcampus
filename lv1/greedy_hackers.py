def solution(N):
    cnt = 0
    coin = [500, 100, 50, 10]
    for i in coin:
        cnt += N // i
        N %= i
    return cnt
N = 1260
print(solution(N))