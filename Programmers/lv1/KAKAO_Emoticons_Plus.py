def solution(users, emoticons):
    answer = [0, 0]
    per = [10, 20, 30, 40]
    discount = []

    # 할인율 구하기
    def dfs(temp, depth):
        # print("<dfs> 1. temp = {0} / depth = {1}".format(temp, depth))
        if depth == len(temp):
            discount.append(temp[:])
            # print(" ** <dfs> 2. discount = {0}".format(discount))
            return
        for d in per:
            # print("<dfs> 3. d = ", d)
            temp[depth] += d
            # print("<dfs> 4. temp[depth] += d")
            # print(">>> temp[{0}] += {1} === {2}".format(depth, d, temp[depth]))
            dfs(temp, depth + 1)
            temp[depth] -= d
            # print(" ================================== ")
            # print(" ** <dfs> 5. temp[depth] -= d")
            # print(">>> temp[{0}] -= {1} === {2}".format(depth, d, temp[depth]))
            # print(" ******* temp = {0} *******".format(temp))
    dfs([0] * len(emoticons), 0)

    # 완전 탐색
    for d in range(len(discount)):
        # print("********* len(discount) = {0}*********".format(len(discount)))
        join, price = 0, [0] * len(users)
        # print("<solution> 1. join = {0}, price = {1}".format(join, price))
        for e in range(len(emoticons)):
            for u in range(len(users)):
                # print("<solution> 2. e = {0}, u = {1}".format(e, u))
                # 할인율을 만족하면 구매
                if users[u][0] <= discount[d][e]:
                    # print("<solution> 3. users[u][0] <= discount[d][e]")
                    # print(">>> users[{0}][0] -> {3} <= discount[{1}][{2}] -> {4}".format(u, d, e, users[u][0], discount[d][e]))
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100
        # 구매 금액에 따라 가입자를 갱신
        for u in range(len(users)):
            print("<solution> 4. u = ", u)
            if price[u] >= users[u][1]:
                # print("<solution> 5. price[u] >= users[u][1]")
                # print(">>> price[{0}] -> {1} >= users[{0}][1] -> {2}".format(u, price[u], users[u][1]))
                join += 1
                # print("<solution> 6. join = ", join)
                price[u] = 0
                # print("<solution> 7. price[{0}] = {1}".format(u, price[u]))

        # 최대 가입자, 구매 금액 갱신
        if join >= answer[0]:
            # print("<solution> 8. join -> {0}, answer -> {1}".format(join, answer[0]))
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
                # print("<solution> 9. answer[1] = max(answer[1], sum(price))")
                # print(">>> answer[1] = max({0}, {1})".format(answer[1], sum(price)))
            else:
                answer[1] = sum(price)
                # print("<solution> 10. answer[1] = sum(price)")
                # print(">>> answer[1] = {0}".format(sum(price)))
            answer[0] = join
            # print("<solution> 11. answer[0] = {0}".format(join))
    return answer

users = [40, 10000], [25, 10000]
emoticons = [7000, 9000]

print(solution(users, emoticons))






