def solution(babbling):
    count = 0
    babble = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in babble:
            print("1. babbling(i) = {0} / babble(j) = {1}".format(i, j))
            if j * 2 not in i:
                i = i.replace(j, ' ')
                print("2. replace babbling(i) = {0}".format(i))
        if i.strip() == '':
            count += 1
            print("3. count = {0}".format(count))
    return count

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))