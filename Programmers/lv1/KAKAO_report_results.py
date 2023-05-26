from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)
    # print(report, user, cnt)

    for r in report:
        a, b = r.split()
        user[a].add(b)
        cnt[b] += 1

    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)

    return answer

def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}
    # print(reports)

    for r in set(report):
        reports[r.split()[1]] += 1
        # print(reports)

    for r in set(report):
        print(r.split())
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
            print(answer)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
# print(solution2(id_list, report, k))
print(solution(id_list, report, k))