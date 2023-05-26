def solution(s):
    zero = 0 # 0의 갯수
    conver = 0 # 변환 횟수

    # s가 '1'이 될때
    while s != '1':
        # 0의 갯수를 카운트해서
        if '0' in s:
            zero += s.count('0') # 0의 숫자 카운트해서 누적
            s = s.replace('0', '') # 0을 전부 공백으로 변경
        s = str(format(len(s), 'b'))
        conver += 1
    return [conver, zero]

def solution2(s):
    cnt, num = 0, 0
    while s != '1':
        print(s)
        cnt += s.count('0')
        length = s.count('1')
        s = bin(length)[2:]
        num += 1
        print("cnt = {0} / length = {1} / s = {2} / num = {3}".format(cnt, length, s, num))
    return [num, cnt]

def solution3(s):
    cnt, zero = 0, 0
    while True:
        if s == '1':
            break
        zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt += 1
    return [cnt, zero]

s = "110010101001"
print(solution3(s))