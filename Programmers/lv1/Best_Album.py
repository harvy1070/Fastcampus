def solution(genres, plays):
    answer = []
    temp = []
    total_genre_d = {}

    temp = [[genres[i], plays[i], i] for i in range(len(genres))]
    print("=============== temp = {0} ===============".format(temp))
    temp = sorted(temp, key = lambda x : (x[0], -x[1], x[2]))
    print("=============== temp = {0} ===============".format(temp))
    for g in temp:
        if g[0] not in total_genre_d:
            total_genre_d[g[0]] = g[1]
            print("1-1. total_genre_d[g[0]] = g[1]")
            print(">>> total_genre_d[{0}] = {1} === {2}".format(g[0], g[1], total_genre_d[g[0]]))
        else:
            total_genre_d[g[0]] += g[1]
            print("1-2. total_genre_d[g[0]] += g[1]")
            print(">>> total_genre_d[{0}] += {1} === {2}".format(g[0], g[1], total_genre_d[g[0]]))

    total_genre_d = sorted(total_genre_d.items(), key = lambda x : -x[1])
    print("*********** total_genre_d = {0} ***********".format(total_genre_d))
    for i in total_genre_d:
        count = 0
        for j in temp:
            print("=========== i = {0}, j = {1}, count = {2} ===========".format(i, j, count))
            if i[0] == j[0]:
                print("2-2. i[0]:{0} == j[0]:{1}".format(i[0], j[0]))
                count += 1
                print("2-2. count = {0}".format(count))
                if count > 2:
                    break
                    print("3-1. count > 2 >>> break")
                else:
                    answer.append(j[2])
                    print("3-2. answer.append(j[2])")
                    print(">>> answer.append({0}) : {1}".format(j[2], answer))
    return answer

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))