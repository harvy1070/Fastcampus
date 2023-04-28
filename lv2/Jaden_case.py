# capitalize >> 첫 문자가 알파벳일 경우 대문자로 만들고 두 번째부턴 자동 소문자 return
# 첫 문자가 알파벳이 아닐 경우 그대로 return 시켜주는 내장 함수
def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return ' '.join(s)

def solution2(s):
    answer=''
    s=s.split(' ')
    for i in range(len(s)):
        if not s[i][0].isdecimal():
            s[i]=s[i][0].upper()+s[i][1:].lower()
    answer=' '.join(s)
    return answer

def solution3(s):
    if len(s) == 0:
        return ""
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][0].upper() + s[i][1:].lower()
        print("s[{0}] = {1} + {2}".format(i, s[i][0], s[i][1:]))
    return " ".join(s)

s = "3people unFollowed me"
print(solution3(s))