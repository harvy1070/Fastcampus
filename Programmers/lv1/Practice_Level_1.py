def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        if count == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key = lambda t : t[1], reverse = True)
    print(answer)
    answer = [i[0] for i in answer]
    print(answer)
    return answer

def solution2(N, stages):
    result = {}
    length = len(stages)
    for i in range(1, N+1):
        if length != 0:
            count = stages.count(i)
            result[i] = count / length
            length -= count
        else:
            result[i] = 0
    return sorted(result, key = lambda x : result[x], reverse=True)


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution2(N, stages))