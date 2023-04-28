# 카카오 괄호 변환
def solution(p):
    if p == "":
        return ""
    else:
        return func(p)

def func(p):
    if p == "":
        return ""
    left, right = 0, 0
    u, v = "", ""
    for i in range(len(p)):
        #print("<func> 1. (func)i = ", i)
        #print("<func> 1-1. p[i] = ", p[i])
        if p[i] == "(":
            left += 1
            #print("<func> 2. (if)left = ", left)
        else:
            right += 1
            #print("<func> 3. (else)right = ", right)
        if left == right:
            u = p[:i+1]
            #print("<func> 4. (if)u = ", u)
            v = p[i+1:]
            #print("<func> 5. (if)v = ", v)
            break
    if right_bracket(u):
        u += func(v)
        #print("<func> 6. [right_b] (if)u = ", u)
        return u
    else:
        string = "(" + func(v) + ")"
        #print("<func> 7. [right_b] (else) string = ", string)
        u = u[1:len(u) - 1]
        #print("<func> 8. [right_b] (else) u = ", u)
        u = reverse_bracket(u)
        #print("<func> 9. [reverse_b] (else) u = ", u)
        string += u
        #print("<func> 10. [right_b] (else) string += u = ", string)
        return string

def right_bracket(p):
    stack = []
    for c in p:
        #print("<right_b> 1. c = ", c)
        #print("<right_b> 1-1. len(stack) = ", len(stack))
        if len(stack) == 0:
            if c == "(":
                stack.append(c)
                #print("<right_b> 2. (if/if)stack = ", stack)
            else:
                return False
        else:
            if c == "(":
                stack.append(c)
                #print("<right_b> 3. (else/if)stack = ", stack)
            else:
                stack.pop()
                #print("<right_b> 4. (else/else)stack = ", stack)
    if len(stack) == 0:
        return True
    else:
        return False

def reverse_bracket(p):
    fixed_p = ""
    for s in p:
        #print("<reverse_b> 1. s = ", s)
        if s == "(":
            fixed_p += ")"
            #print("<reverse_b> 2. (if)fixed_p = ", fixed_p)
        else:
            fixed_p += "("
            #print("<reverse_b> 3. (else)fixed_p = ", fixed_p)
    return fixed_p

def solution2(p):
    if p == '':
        return p
    r = True
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1
        if c > 0:
            r = False
        if c == 0:
            if r:
                return p[:i+1] + solution(p[i+1:])
            else:
                return '(' + solution(p[i+1:]) + ')' + ''.join(list(map(lambda x:'(' if x == ')' else ')', p[1:i])))
p = "()))((()"
print(solution2(p))
