def solution(s):
    answer = ''
    for i in s:
        if i == ')':
            return False
        elif i == '(':
            if s.count('(') == s.count(')'):
                return True

def solution_re(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()

    if stack != []:
        return False
    return True

s = ")()("
print(solution_re(s))