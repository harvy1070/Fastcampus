# def solution(survey, choices):
#     answer = ''
#     dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
#     for s, c in zip(survey, choices):
#         print("1. s = {0} / c = {1}".format(s, c))
#         if c > 4:
#             dic[s[1]] += c - 4
#             print("2-1(c > 4). dic[{0}] += {1} - 4 >>> {2}".format(s[1], c, dic[s[1]]))
#         elif c < 4:
#             dic[s[0]] += 4 - c
#             print("2-2(c < 4). dic[{0}] += 4 - {1} >>> {2}".format(s[0], c, dic[s[0]]))
#
#     print("3-1. dic = {0}".format(dic))
#     li = list(dic.items())
#     print("3-2. li = {0}".format(li))
#
#     for i in range(0, 8, 2):
#         if li[i][1] < li[i+1][1]:
#             answer += li[i+1][0]
#             print("4-1. li[{0}][1]:{1} < li[{0}+1][1]:{2}".format(i, li[i][1], li[i+1][1]))
#             print(">>> answer += li[{0}+1][0] >>> answer = {1}".format(i, answer))
#         else:
#             answer += li[i][0]
#             print("4-2. else")
#             print(">>> answer += li[{0}][0] >>> answer = {1}".format(i, answer))
#
#     print("5. answer = {0}".format(answer))
#     return answer

def solution(survey, choices):
    answer = ''
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':2, 'A':1, 'N':1}

    for s, c in zip(survey, choices):
        if c > 4:
            dic[s[1]] += c - 4
        elif c < 4:
            dic[s[0]] += 4 - c

    ld = list(dic.items())

    for i in range(0, 8, 2):
        if ld[i][1] < ld[i+1][1]:
            answer += ld[i+1][0]
        else:
            answer += ld[i][0]

    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))