# 거스름돈
# n = 1260
# count = 0
#
# coin_types = [500, 100, 50, 10]
#
# for coin in coin_types:
#     count += n // coin
#     n %= coin
#     print(n)
#
# print(count)

# n에 들어간 수에서 m 만큼 반복해서 더한 최대값 구하기(연속된 수 제한은 k)
# n, m, k = map(int, input().split())
#
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         print("result1 = ", result)
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     print("result2 = ", result)
#     m -= 1
# print(result)

# greedy 방법 2(for문 사용 x)
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n - 1]
# second = data[n - 2]
#
# count = int(m / (k+1)) * k
# count += m % (k+1)
#
# result = 0
# result += (count) * first
# result += (m - count) * second
#
# print(result)

## card game1
# n, m = map(int, input().split())
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
#
#     result = max(result, min_value)
# print(result)

# # card game2
# n, m = map(int, input().split())
#
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     #print(data)
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
#         print(min_value)
#
#     result = max(result, min_value)
# print(result)

# # 1이 될 때 까지 나누기 (1)
# n, k = map(int, input().split())
# result = 0
#
# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#
#     n //= k
#     result += 1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)

# 1이 될때까지 나누기 (2)
# n, k = map(int, input().split())
# result = 0
#
# while True:
#     target = (n//k) * k
#     print("target = ", target)
#     result += (n-target)
#     print("result = ", result)
#     n = target
#     print("n = ", n)
#
#     if n < k:
#         break
#
#     result += 1
#     n //= k
#     print("n2 = ", n)
#
# result += (n-1)
# print(result)







