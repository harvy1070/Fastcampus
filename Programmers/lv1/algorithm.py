# 소수 판별 알고리즘
# def is_prime_number(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
# print(is_prime_number(4))
# print(is_prime_number(7))

# sqrt를 활용하여 소수 판별
# import math
# def is_prime_number2(x):
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True
#
# print(is_prime_number2(4))
# print(is_prime_number2(7))

# 에라토스테네스의 체 / 여러 개의 수가 소수인지 아닌지 판별할 때 사용

# import math
# n = 1000
# array = [True for i in range(n+1)]
#
# for i in range(2, int(math.sqrt(n)+1)):
#     if array[i] == True:
#         j = 2
#         while i * j <= n:
#             array[i*j] = False
#             j += 1
#
#         for i in range(2, n+1):
#             if array[i]:
#                 print(i, end='')

# two pointer algorithm / 시작값, 끝값 위치 설정하여 m 과 비교하여 m을 넘으면 end 값의 위치를 변경
# n = 5
# m = 5
# data = [1,2,3,2,5]
#
# cnt = 0
# interval_sum = 0
# end = 0
#
# for start in range(n):
#     #print("start = ", start)
#     while interval_sum < m and end < n:
#         #print("interval_sum, end = ", interval_sum, end)
#         interval_sum += data[end]
#         #print("(+=data[end])interval_sum = ", interval_sum)
#         end += 1
#
#     if interval_sum == m:
#         cnt += 1
#
#     interval_sum -= data[start]
# print(cnt)

# 정렬된 두 리스트의 합집합
# n, m = 3, 4
# a = [1,3,5]
# b = [2,4,6,8]
#
# result = [0] * (n + m)
# i, j, k = 0, 0, 0
#
# while i < n or j < m:
#     if j >= m or (i < n and a[i] <= b[j]):
#         result[k] = a[i]
#         i += 1
#
#     else:
#         result[k] = b[j]
#         j += 1
#     k += 1
#
# for i in result:
#     print(i, end='')

# import math
#
# m, n = map(int, input().split())
# arr = [True for i in range(1000001)]
# arr[1] = 0 # 1은 소수가 아님
#
# # 에라토스테네스의 체 알고리즘
# for i in range(2, int(math.sqrt(n))):
#     if arr[i] == True:
#         j = 2
#         while i * j <= n:
#             print(i, j)
#             arr[i*j] = False
#             j += 1
#
# for i in range(m, n+1):
#     if arr[i]:
#         print(i)

# 암호문 만들기
from itertools import combinations
v = ('a', 'e', 'i', 'o', 'u') # 5개 모음 정의
l, c = map(int, input().split(' '))

arr = input().split(' ')
arr.sort()

for pw in combinations(arr, l):
    cnt = 0
    for i in pw:
        if i in v:
            cnt += 1

    if cnt >= 1 and cnt <= l - 2:
        print(''.join(pw))

print(cnt)


