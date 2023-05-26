def solution(keymap, targets):
    answer = []
    dic = {}

    for i in keymap:
        tmp = list(set(list(i)))
        for j in tmp:
            if j in dic:
                dic[j] = min(dic[j], i.index(j)+1)
            else:
                dic[j] = i.index(j) + 1

    for i in targets:
        tmp = 0
        for j in i:
            if j in dic:
                tmp += dic[j]
            else:
                tmp += 1
                break
        answer.append(tmp)

    return answer

def solution2(keymap, targets):
    answer = []
    for i in targets:
        tmp = 0
        for alpha in i:
            position = 1000
            for index, k in enumerate(keymap):
                if alpha in k and (k.index(alpha) < position and position > -1):
                    position = k.index(alpha) + 1
            if position == 1000:
                tmp = -1
                break
            else:
                tmp += position
        answer.append(tmp)
        print(answer)
    return answer

def solution3(keymap, targets):
    min_stroke = dict()
    for key in keymap:
        for idx, alpha in enumerate(key):
            print(min_stroke)
            if alpha in min_stroke.keys():
                if idx + 1 < min_stroke[alpha]:
                    min_stroke[alpha] = idx + 1
            else:
                min_stroke[alpha] = idx + 1
    answer = []
    for target in targets:
        total_stroke = 0
        for alpha in target:
            if alpha in min_stroke:
                total_stroke += min_stroke[alpha]
            else:
                total_stroke = -1
                break
        answer.append(total_stroke)
    return answer


keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
print(solution3(keymap, targets))