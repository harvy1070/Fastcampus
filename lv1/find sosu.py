from itertools import permutations
# 소수 판별하는 함수로 판별하기
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**(1/2)) + 1):
#         print("5. (is_prime) i = ", i)
#         if n % i == 0:
#             return False
#
#     return True
#
# def solution(numbers):
#     answer = set()
#
#     numbers = list(i for i in numbers)
#     print("1. (list)numbers = ", numbers)
#     for i in range(1, len(numbers)+1):
#         print("2. (for)i = ", i)
#         arr = list(map(''.join, permutations(numbers, i)))
#         print("3. (permutations)arr = ", arr)
#         for j in arr:
#             print("4. (arr)j = ", j)
#             if is_prime(int(j)):
#                 answer.add(int(j))
#                 print("6. (add(int(j))answer = ", answer)
#     return len(answer)

# 재귀함수로 판별하기
primeSet = set()
def is_Prime(n):
    if n in (0, 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def make_Combinations(str1, str2):
    print("<m_C>str1, str2 = ", str1, str2)
    if str1 != "":
        if is_Prime(int(str1)):
            print("<m_C>int(str1) = ", int(str1))
            primeSet.add(int(str1))
    for i in range(len(str2)):
        make_Combinations(str1 + str2[i], str2[:i] + str2[i + 1:])

def solution(numbers):
    make_Combinations("", numbers)
    answer = len(primeSet)
    return answer















numbers = "17"
print(solution(numbers))