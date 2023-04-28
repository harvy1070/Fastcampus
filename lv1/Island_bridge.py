def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])
    print("=== costs = {0} ===".format(costs))
    link = set([costs[0][0]])
    print("=== link = {0} ===".format(link))

    while len(link) != n:
        print("1. len(link) = {0}".format(len(link)))
        for v in costs:
            print("2. v:{0}".format(v))
            print("=== link = {0} ===".format(link))
            if v[0] in link and v[1] in link:
                print("3-1. if v[0] in link and v[1] in link")
                print(">>> {0} in {1} and {2} in {1}".format(v[0], link, v[1]))
                continue
            if v[0] in link or v[1] in link:
                print("3-2. if v[0] in link or v[1] in link")
                print(">>> {0} in {1} or {2} in {1}".format(v[0], link, v[1]))
                link.update((v[0], v[1]))
                print("3-3. link = {0}".format(link))
                answer += v[2]
                print("3-4. answer = {0}".format(answer))
                break
    return answer

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution(n, costs))