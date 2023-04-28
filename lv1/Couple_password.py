from string import ascii_lowercase

def solution(s, skip, index):
    result = ''
    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}
    # print(dic_alpha)

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]
    return result

s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))
