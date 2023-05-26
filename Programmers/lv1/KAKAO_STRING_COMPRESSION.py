def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        print("1. i = ", i)
        cnt = 1
        cur = ''
        temp = s[:i]
        print("2. temp(s[:{0}]) = {1}".format(i, s[:i]))
        for j in range(i, len(s), i):
            print("3. j = ", j)
            print("4. temp(s[{0}:{0}+{1}]) = {2}".format(j, i, s[j:j+i]))
            if temp == s[j:j+i]:
                cnt += 1
                print("5. <if> cnt = ", cnt)
            else:
                if cnt == 1: # 압축 불가능할 때
                    cur += temp
                    print("6. <else/if> cur = ", cur)
                else: # 압축 가능할 때
                    cur += str(cnt) + temp
                    print("7. <else/else> cur = ", cur)
                cnt = 1
                print("8. <reset> cnt = ", cnt)
                temp = s[j:j+i] # 여기부터 다시
        if cnt == 1:  # 남은 것들 flush
            cur += temp
            print("9. <if> cur = ", cur)
        else:
            cur += str(cnt) + temp
            print("10. <else> cur = ", cur)
        answer = min(answer, len(cur)) # 길이 갱신
    return answer

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    print("words = ", words)
    res = []
    cur_word = words[0]
    cur_cnt = 1

    for a, b in zip(words, words[1:] + ['']):
        print("a = {0} / b = {1}".format(a, b))
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            print("res = ", res)
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution2(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2)+1)) + [len(text)])

text = "ababcdcdababcdcd"
s = "ababcdcdababcdcd"
print(solution2(s))