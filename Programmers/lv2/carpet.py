def solution(brown, yellow):
    answer = []
    total = brown + yellow  # a * b = total
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:  # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [int(a), int(b)]
    return int(answer)

def solution2(brown, yellow):
    for i in range(1, int(yellow ** (1/2)+1)):
        if yellow % i == 0:
            if 2 * (i+yellow//i) == brown - 4:
                return [yellow//i+2, i+2]

brown, yellow = 10, 2
print(solution2(brown, yellow))