def solution(s):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dict = {}
    for i in range(len(num_list)):
        dict[num_list[i]] = i

    result = ''
    eng = ''

    for i in s:
        if i.isdigit():
            result += i
        elif i.isalpha():
            eng += i
            if eng in dict:
                result += str(dict[eng])
                eng = ''
    return result


s = "onetwo2fivefour9"
print(solution(s))