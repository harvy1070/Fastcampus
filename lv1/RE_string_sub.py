def solution(s):
    answer = 0
    ls = list(s)
    cnt_l = ["", 1, 0]
    index = 1

    while len(ls) > 0:
        if len(ls) == index:
            answer += 1
            break
        cnt_l[0] = ls[0]
        if ls[index] == cnt_l[0]:
            cnt_l[1] += 1
            index += 1
        else:
            cnt_l[2] += 1
            if cnt_l[1] == cnt_l[2]:
                del ls[:index+1]
                answer += 1
                index, cnt_l[1], cnt_l[2] = 1, 1, 0
            else:
                index += 1
    return answer

def solution2(s):
    answer = 0
    t = ["", 0, 0]
    for i in s:
        if t[0] == "":
            t[0] = i
            t[1] += 1
        else:
            if t[0] == i:
                t[1] += 1
            else:
                t[2] += 1
            if t[1] == t[2]:
                answer += 1
                t = ["", 0, 0]
    if t != ["", 0, 0]:
        answer += 1
    return answer

s = "aaabbaccccabba"
print(solution(s))