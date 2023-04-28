from collections import Counter
def solution(topping):
    answer = 0
    me = Counter(topping)
    bro = {}

    for i in range(len(topping)):
        print("1. i = ", i)
        if topping[i] in bro:
            bro[topping[i]] += 1
            print("2. <if> bro[topping[{0}]] = {1}".format(i, bro[topping[i]]))
        else:
            bro[topping[i]] = 1
            print("3. <else> bro[topping[{0}]] = {1}".format(i, bro[topping[i]]))
        me[topping[i]] -= 1
        print("4. me[topping[{0}] = {1}".format(i, me[topping[i]]))

        if me[topping[i]] == 0:
            print("5. <if2> me[topping[{0}] = {1}".format(i, me[topping[i]]))
            del me[topping[i]]

        if len(bro) == len(me):
            print("6. <if3> len(bro) = {0}, len(me) = {1}".format(len(bro), len(me)))
            answer += 1
            print("7. <if3> answer = ", answer)
    return answer

def solution2(topping):
    answer = 0
    dic = Counter(topping)
    print("1. dic = ", dic)
    set_dic = set()
    print("2. set_dic = ", set_dic)

    for i in topping:
        print("3. i = ", i)
        dic[i] -= 1
        print("4. dic[{0}] = {1}".format(i, dic[i]))
        set_dic.add(i)
        print("5. set_dic.add({0}) = {1}".format(i, set_dic))
        if dic[i] == 0:
            print("6. dic.pop({0}) = {1}".format(i, dic))
            dic.pop(i)
        if len(dic) == len(set_dic):
            print("7. answer = ", answer)
            answer += 1
    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution2(topping))