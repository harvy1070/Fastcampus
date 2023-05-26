def solution(order):
    temp = []
    i = 1
    now = 0

    while i != len(order)+1:
        print("1. i = {0} / len(order)+1 = {1}".format(i, len(order)+1))
        temp.append(i)
        print("2. temp = {0} / i = {1}".format(temp, i))
        while temp[-1] == order[now]:
            print("*** order *** = ", order)
            print("*** temp *** = ", temp)
            print("3. temp[-1] = {0} / order[{1}] = {2}".format(temp[-1], now, order[now]))
            now += 1
            print(" === now = {0} === ".format(now))
            temp.pop()

            if len(temp) == 0:
                break
        i += 1

    return now

order = [1, 2, 3, 4, 5]
print(solution(order))
