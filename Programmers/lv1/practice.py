# 1 - 9 제곱
# a = [i * i for i in range(1, 10)]
# print(a)

# a = []
# for i in range(1, 10):
#     a.append(i * i)
#
# print(a)

# 2차원배열
# n = 3
# m = 4
# a = [[0] * m for _ in range(n)]
# print(a)

# 2차원 배열 초기화
# n = 3
# m = 4
# array = [[0] * m] * n
# print(array)
#
# array[0][1] = 5
# print(array)

# list 메서드
# a = [1, 4, 3]
# print("base = ", a)
#
# a.append(2)
# print("apppend = ", a)
#
# a.sort()
# print("sort = ", a)
#
# a.reverse()
# # a.sort(reverse = True)와 같음
# print("reverse = ", a)
#
# a.insert(2, 3)
# print("index 2에 3추가 = ", a)
#
# # count
# print("count = ", a.count(3))
#
# a.remove(1)
# print("remove = ", a)

# remove_set
# a = [1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5}
# result = []
# for i in a:
#     if i not in remove_set:
#         result.append(i)
# print(result)

# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#
# key_list = data.keys()
# value_list = data.values()
# print(key_list)
# print(value_list)
#
# for key in key_list:
#     print(data[key])
#
# data = set([1,1,2,3,4,4,5])
# print(data)
#
# a = set([1,2,3,4,5])
# b = set([3,4,5,6,7])
#
# print(a|b) # 합집합
# print(a&b) # 교집합
# print(a-b) # 차집합
#
# data = set([1,2,3])
# print(data)
#
# data.add(4)
# print(data)
#
# data.update([5,6])
# print(data)
#
# data.remove(3)
# print(data)

# score = 95
# if score >= 70:
#     print('성적 70점 이상')
#     if score >= 90:
#         print('우수')
# else:
#     print('성적 70점 미만')
#
# print('program exit')

# a = [1,2,3,4,5,5,5]
# remove_set = {3,5}
#
# #result = []
# # for i in a:
# #     if i not in remove_set:
# #         result.append(i)
#
# # 위 for문을 한줄식으로
# result = [i for i in a if i not in remove_set]
# print(result)

# while문
# i = 1
# result = 0
#
# while i <= 9:
#     result += i
#     i += 1
#
# print(result)

# 홀수만 더하는 while문
# i = 1
# result = 0
#
# while i <= 9:
#     if i % 2 == 1:
#         result += i
#         print(result)
#     i += 1
# print(result)

# for문
# result = []
# for i in range(1, 11):
#     result.append(i)
# print(result)

# scores = [90, 85, 77, 65, 97]
# cheating_list = [2, 4]
# if 문에 continue로 cheating_list에 해당되는 i+1번은 그냥 무시하고 다음번호부터 처리하게함
# for i in range(len(scores)):
#     if i + 1 in cheating_list:
#         continue
#     if scores[i] >= 85:
#         print(i+1, "번 합격")

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i, 'X', j, '=', i*j)

# ==  function == #
# a = 0
# def func():
#     global a
#     a += 1
#
# for i in range(10):
#     func()
#
# print(a)

# iostream / input output

# n = int(input())
#
# data = list(map(int, input().split()))
#
# data.sort(reverse = True)
# print(data)

# 공백 기준 구분하여 적은 수 데이터 입력
# n, m, k = map(int, input().split())
#
# print(n, m, k)

# 1 line input

# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# f-string을 이용한 변수 자료형 변경 없이 바로 출력하기
# answer = 7
# print(f"정답은 {answer}입니다.")

# in function
# result = sum([1,2,3,4,5])
# print(result)

# eval을 이용한 문자열 형태의 수식 자동 계산
# ff = "(3+5) * 7"
# result = eval(ff)
# print(result)

# dictionary에서 values 값을 기준으로 정렬하기
# result = sorted([('홍길동', 35), ('이순신', 75), ('이무개', 50)], key = lambda x:x[1], reverse = True)
# print(result)

# data = [9, 1, 8, 5, 4]
# data.sort()
# print(data)

# 반복되는 데이터 처리 itertools (permutations, combinations)

# from itertools import permutations
# data = ['A', 'B', 'C']
# result1 = list(permutations(data, 3)) # 순열
# print("permutations = ", result1)
#
# from itertools import combinations
# result2 = list(combinations(data, 2)) # 순서 고려x 조합에 대해서만 출력, 중복 허용하지 않음
# print("combination = ", result2)
#
# from itertools import product
# result3 = list(product(data, repeat = 2)) # 중복을 포함한 모든 경우의 수 출력 ex) A, B = B, A
# print("product = ", result3)
#
# from itertools import combinations_with_replacement
# result4 = list(combinations_with_replacement(data, 2)) # 리스트에서 중복을 포함하여 정해진 갯수를 뽑아 순서에 상관없이 모두 나열
# print("cwr = ", result4)

# heapq heappush() = 원소 삽입 heappop() 원소 꺼내기

# heappop과 heappush를 이용한 오름차순 정렬
# import heapq
# def heapsort(iterable):
#     h = []
#     result = []
#
#     for value in iterable:
#         heapq.heappush(h, value)
#         print("heappush = ", value)
#     print("heapq = ", h)
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#         print("heappop = ", result)
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

# heapq를 이용한 역순으로 정렬하기(내림차순)
# import heapq
# def heapsort(iterable):
#     h = []
#     result = []
#
#     for value in iterable:
#         heapq.heappush(h, -value)
#
#     for _ in range(len(h)):
#         result.append(-heapq.heappop(h))
#
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

# bisect 이진탐색 구현
# bisect_left(a, x) 정렬 순서 유지, 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 서치 <=> bisect_right

from bisect import bisect_left, bisect_right
# a = [1,2,4,4,8]
# x = 4
#
# print(bisect_left(a, x))
# print(bisect_right(a, x))

# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     print("right_index = ", right_index)
#     left_index = bisect_left(a, left_value)
#     print("left_index = ", left_index)
#     return right_index - left_index
#
# a = [1,2,3,3,3,3,4,4,8,9]
# # 값이 4인 데이터 갯수 출력
# print(count_by_range(a, 4, 4))
# # 값이 [-1, 3] 범위에 있는 데이터 개수 출력
# print(count_by_range(a, -1, 3))

# deque
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(list(data))

# Counter / 등장 횟수 세기
from collections import Counter
c = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(c['blue'])
print(dict(c))

# math
# math.factorial / 팩토리얼
import math
print(math.factorial(5))

# math.sqrt / 제곱근
print(math.sqrt(4))

# math.gcd / 최대 공약수
print(math.gcd(21, 14))

# math.pi
print(math.pi)
print(math.e)








