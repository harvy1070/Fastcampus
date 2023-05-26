# def solution(number, limit, power):
#     count = 0
#     result = []
#     res = []
#
#     for i in range(1, number+1):
#         if i == 1:
#             result.append(1)
#         else:
#             for j in range(1, i+1):
#                 if i % j == 0:
#                     count += 1
#                 else:
#                     continue
#             if count > limit:
#                 result.append(power)
#                 count = 0
#             else:
#                 result.append(count)
#                 count = 0
#     return sum(result)

# def solution(number, limit, power):
#     answer = 0
#     def count_nums(a):
#         cnt = 0
#         for i in range(1, int(a**(1/2)) + 1):
#             print(int(a**(1/2)))
#             if a % i == 0:
#                 cnt += 1
#                 if ((i ** 2) != a):
#                     cnt += 1
#             if cnt > limit:
#                 return power
#         return cnt
#
#     for i in range(1, number+1):
#         k = count_nums(i)
#         if k > limit:
#             k = power
#         answer += k
#     return answer

# def solution(number, limit, power):
#     answer = 0
#     for i in range(1, number+1):
#         cnt = 0
#         for j in range(1, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 cnt += 1
#                 if i // j != j:
#                     cnt += 1
#             if cnt > limit:
#                 break
#         if cnt > limit:
#             answer += power
#         else:
#             answer += cnt
#     return answer

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        print(i ** 0.5)
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                if i // j != j:
                    print("{0} // {1} != {1}".format(i, j))
                    count += 1
            if count > limit:
                break
        if count > limit:
            answer += power
        else:
            answer += count
    return answer

number = 10
limit = 3
power = 2
print(solution(number, limit, power))