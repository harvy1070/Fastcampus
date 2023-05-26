def solution(name, yearning, photo):
    data = dict(zip(name, yearning))
    answer = []
    for p in photo:
        result = 0
        for key in p:
            if type(data.get(key)) == int:
                result += data.get(key)
        answer.append(result)
    return answer



name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo))