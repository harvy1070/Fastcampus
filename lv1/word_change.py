from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    v = [0 for i in range(len(words))]
    #print("1. q = {0}, v = {1}".format(q, v))

    while q:
        word, cnt = q.popleft()
        #print("2. word = {0}, cnt = {1}".format(word, cnt))
        if word == target:
            answer = cnt
            #print("3. word({0}) = target({1}) >>> answer = cnt:{2}".format(word, target, cnt))
            break
        #print("************** words = {0}, word = {1} **************".format(words, word))
        for i in range(len(words)):
            #print("4. <for(len(words)> i = {0}".format(i))
            temp_cnt = 0
            if not v[i]:
                #print("5. not v[i] = {0}".format(v[i]))
                for j in range(len(word)):
                    print("************** words = {0}, word = {1}, v = {2} **************".format(words, word[j], v))
                    #print("6. <for(len(word)> j = {0}".format(j))
                    if word[j] != words[i][j]:
                        #print("7. word[j] != words[{0}][{1}] >>> {2}".format(i, j, words[i][j]))
                        temp_cnt += 1
                        #print("8. temp_cnt = {0}".format(temp_cnt))
                if temp_cnt == 1:
                    q.append([words[i], cnt + 1])
                    #print("9. q.append([words[i], cnt + 1])")
                    #print(">>> q = {0} / words[{1}] > {2}, cnt + 1 > {3}".format(q, i, words[i], cnt+1))
                    v[i] = 1
    return answer

begin = "hit"
target = "dog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))