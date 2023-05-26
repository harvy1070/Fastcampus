def solution(n):
    answer = [0, 3, 11]
    index = int(n/2)
    print("1. index = {0}".format(index))
    if n % 2 != 0:
        return answer[0]
    if index < 3:
        print(">>> answer[{0}] = {1}".format(index, answer[index]))
        return answer[index]

    for i in range(3, index+1):
        answer.append((3*answer[i-1] + sum(answer[1:i-1])*2+2)%1000000007)
        print(">>> answer = {0}".format(answer))
    return answer[index]

n = 10
print(solution(n))