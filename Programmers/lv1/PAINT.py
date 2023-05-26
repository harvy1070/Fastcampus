# def solution(n, m, section):
#     cnt = 0
#
#     while section:
#         end = section[-1] - 1
#         start = end - m + 1
#
#         if start < 0:
#             start, end = 0, m-1
#         cnt += 1
#         while start <= (section[-1] - 1):
#             section.pop()
#             if not section:
#                 break
#     return cnt

def solution(n, m, section):
    answer, painted = 0, 0
    for i in section:
        print(i)
        if i >= painted:
            painted = i + m
            answer += 1
    return answer

n, m = 8, 4
section = [2, 6, 7]
print(solution(n, m, section))