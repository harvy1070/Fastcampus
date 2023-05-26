def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n%3)
            n //= 3
            print("(if)answer = ", answer)
            print("n = ", n)
        else:
            answer += "4"
            print("(else)answer = ", answer)
            n = n//3 - 1
            print("(else)n = ", n)
    return answer[::-1]

n = 7
print(solution(n))