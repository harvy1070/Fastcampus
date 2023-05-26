# def solution(dartResult):
#     n = ''
#     score = []
#     for i in dartResult:
#         if i.isnumeric():
#             n += i
#         elif i == 'S':
#             n = int(n) ** 1
#             score.append(n)
#             n = ''
#         elif i == 'D':
#             n = int(n) ** 2
#             score.append(n)
#             n = ''
#         elif i == 'T':
#             n = int(n) ** 3
#             score.append(n)
#             n = ''
#         elif i == '*':
#             if len(score) > 1:
#                 score[-2] = score[-2] * 2
#                 score[-1] = score[-1] * 2
#             else:
#                 score[-1] = score[-1] * 2
#         elif i == '#':
#             score[-1] = score[-1] * -1
#     return sum(score)

import re
def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'':1, '*':2, '#':-1}
    p = re.compile('(\d)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(p, dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


dartResult = '1S2D*3T'
print(solution(dartResult))