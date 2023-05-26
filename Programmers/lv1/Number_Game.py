def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    print("A = {0} / B = {1}".format(A, B))
    for a in A:
        if a >= B[0]:
            continue
        else:
            answer += 1
            del B[0]
            print("answer = {0} / B = {1}".format(answer, B))
    return answer

A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
print(solution(A, B))