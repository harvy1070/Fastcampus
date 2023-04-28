def solution(name):
    answer = 0

    min_move = len(name) - 1
    print("1. min_move = ", min_move)

    for i, char in enumerate(name):
        print("2. i = {0}, char = {1}".format(i, char))

        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        print(" *** len(name) *** = ", len(name))
        print("min_move = {0} / "
              "2 * i({1}) + len(name) = {2} / "
              "i({1}) + 2 * (len(name) - next({3}) = {4}".format(min_move, i, 2*i+len(name), next, i + 2 * (len(name)-next)))
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    answer += min_move
    return answer

name = 'JAN'
print(solution(name))