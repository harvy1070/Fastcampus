def solution(s):
    if len(s) % 2 == 1: return 0
    if len(s) == 2: return 1 if s[0] == s[1] else 0

    stack = [s[0]]

    for i in s[1:]:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 0 if len(stack) else 1

def solution2(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    return 0

s = "baabaa"
print(solution2(s))