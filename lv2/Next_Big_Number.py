# from collections import Counter
# def two_change(n):
#     if n == 0:
#         print("<two_change> 1. if n == 0: {0}".format(n))
#         return ''
#     elif n % 2 == 0:
#         print("<two_change> 2. if n % 2 == 0: {0}".format(n))
#         print(">>> return two_change({0}//2) + '0' == {1}".format(n, two_change(n // 2) + '0'))
#         return two_change(n//2) + '0'
#     else:
#         print("<two_change> 3. else: two_change({0}//2) + '1' == {1}".format(n, two_change(n // 2) + '1'))
#         return two_change(n//2) + '1'
#
#
# def count_one(n):
#     n = two_change(n)
#     print("<count_one> 1. (two_change(n))n = {0}".format(n))
#     n = Counter(list(n))
#     print("<count_one> 2. (Counter(list(n))n = {0}".format(n))
#     return n['1']
#
# def solution(n):
#     cnt = count_one(n)
#     print("<solution> 1. cnt = {0}".format(cnt))
#     for i in range(n+1, 100000001):
#         if cnt == (count_one(i)): return i

def solution(n):
    c = bin(n).count('1')
    print(c)
    for m in range(n+1, 10000001):
        print(bin(m))
        if bin(m).count('1') == c:
            return m

n = 78
print(solution(n))