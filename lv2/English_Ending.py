def solution(n, words):
    history = [words[0]]
    for i in range(1, len(words)):
        # print("**** i = {0}, words[i] = {1}, history = {2}".format(i, words[i], history))
        # 한 글자인 단어는 인정 안됨
        if len(words[i]) == 1:
            # print("<check == 1>1-1. len(words[{0}]) = {1}".format(i, len(words[i])))
            return [(i%n) + 1, (i+n)//n]
        else:
            # 앞 사람이 말한 단어 끝자리와 일치하는지 여부
            if words[i-1][-1] != words[i][0]:
                # print("<else/if 단어 불일치> 2-1. words[{0}][-1]:{1} != words[{0}][0]:{2}".format(i, words[i-1][-1], words[i][0]))
                # print(">>> [({0}%{1})+1 >> {2}, ({0}+{1})//{1} >> {3}]".format(i, n, (i%n)+1, (i+n)//n))
                return [(i%n) + 1, (i+n)//n]
            else:
                # 이전 단어 검사
                if words[i] in history:
                    # print("<else/else/if> 3-1. words[{0}]:{1} in {2}".format(i, words[i], history))
                    # print(">>> [({0}%{1})+1 >> {2}, ({0}+{1})//{1} >> {3}]".format(i, n, (i%n)+1, (i+n)//n))
                    return [(i%n) + 1, (i+n)//n]
                else:
                    # print("<else/else/else> 3-2. >>> history = {0}".format(history))
                    history.append(words[i])
    return [0, 0]

def solution2(n, words):
    answer = []
    turn = 0
    wordlist = [words[0]]
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordlist:
            turn = idx
            break
        wordlist.append(words[idx])
    answer = [turn%n+1, turn//n+1]
    if turn == 0:
        answer = [0, 0]
    return answer



n = 3
words = ["tank", "kick", "know",
         "wheel", "land", "dream",
         "mother", "robot", "tank"]
print(solution2(n, words))