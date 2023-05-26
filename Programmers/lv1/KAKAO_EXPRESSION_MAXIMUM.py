def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == "*":
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
        print("res(*) = ", res)
    if priority[n] == "+":
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
        print("res(+) = ", res)
    if priority[n] == "-":
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
        print("res(-) = ", res)
    return str(res)

def solution(expression):
    answer = 0
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '-', '*'),
        ('+', '*', '-'),
        ('-', '+', '*'),
        ('-', '*', '+')
    ]
    for priority in priorities:
        res = int(calc(priority, 0 ,expression))
        print("result res = ", res)
        answer = max(answer, abs(res))
        print(answer)

    return answer

def solution2(expression):
    operation = [
        ('+', '-', '*'),
        ('+', '*', '-'),
        ('-', '+', '*'),
        ('-', '*', '+'),
        ('*', '+', '-'),
        ('*', '-', '+')
    ]
    answer = []
    for op in operation:
        a = op[0]
        b = op[1]
        print('1. a:{0} / b:{1}'.format(a, b))
        temp_list = []
        #print('2. temp_list = ', temp_list)
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            print('3. temp = ', temp)
            temp_list.append(f'({b.join(temp)})')
            print('4. temp_list.append = ', temp_list)
        answer.append(abs(eval(a.join(temp_list))))
        print('5. answer = ', answer)
    return max(answer)

expression = "100-200*300-500+20"
print(solution2(expression))
