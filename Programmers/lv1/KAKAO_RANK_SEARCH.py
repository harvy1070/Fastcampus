from bisect import bisect_left
from itertools import combinations
def solution(info, query):
    answer = []
    dic = {}
    comb = [0, 1, 2, 3]
    for i in info:
        person = i.split()
        conditions = person[:-1]
        score = int(person[-1])
        #print("1. i = {0} / person = {1} / conditions = {2} / score = {3}".format(i, person, conditions, score))
        for j in range(5):
            for k in list(combinations(comb, j)):
                temp = conditions.copy()
                #print("1. temp = ", temp)
                for idx in k:
                    temp[idx] = '-'
                    #print("2. temp[idx#{0}] = {1}".format(idx, temp[idx]))
                key = ''.join(temp)
                #print("3. key = ", key)
                if key in dic:
                    dic[key].append(score)
                else:
                    dic[key] = [score]
                #print("dic[{0}] = {1}".format(key, dic[key]))
    for value in dic.values():
        #print("value = ", value)
        value.sort()

    for i in query:
        q_list = []
        for j in i.split():
            if j == 'and':
                continue
            else:
                q_list.append(j)
            #print("q_list = ", q_list)
        target = int(q_list[-1])
        key = ''.join(q_list[:-1])
        if key in dic:
            hubo_list = dic[key]
            print("hubo_list = ", hubo_list)
            index = bisect_left(hubo_list, target)
            print("index = ", index)
            answer.append(len(hubo_list) - index)
        else:
            answer.append(0)
            continue
        print("answer = ", answer)
    return answer

def solution2(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['pizza', 'chicken', '-']:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

    answer = list()
    for q in query:
        q = q.split()
        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l) // 2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid + 1
        answer.append(len(pool) - l)
    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution2(info, query))
