from itertools import combinations as comb

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    print(" === row : {0} / col : {1} === ".format(row, col))
    candidates = []
    # 전체조합
    for i in range(1, col + 1):
        candidates.extend(comb(range(col), i))
        print("<ALL> candidate = ", candidates)

    # 유일성
    unique = []
    for c in candidates:
        temp = [tuple([item[i] for i in c]) for item in relation]
        print("<Uniqueness> temp = ", temp)
        if len(set(temp)) == row:
            unique.append(c)

    # 최소성(set활용)
    answer = set(unique)
    print("<Minimalism> answer = ", answer)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            print("<Minimalism> i = {0} / j = {1} / unique[{0}] = {2} / unique[{1}] = {3}".format(i, j, unique[i], unique[j]))
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
                print("<Minimalism> answer.discard(unique[{0}]) = {1}".format(j, answer.discard(unique[j])))
    return len(answer)

def solution2(relation):
    answer = 0
    all = list()
    unique_index = []
    if len(relation) > 0:
        colSize = len(relation[0])
        rowSize = len(relation)

        # set 형태로 모든 컬럼의 조합 구하기
        for i in range(1, colSize + 1):
            all.extend([set(k) for k in comb([j for j in range(colSize)], i)])
            # set로 중복을 모두 제거한 모든 컬럼의 조합 구함
            # print("all = ", all)

        for c in all:
            validSet = set()
            for rr in range(rowSize):
                temp = ''
                for cc in c:
                    temp += relation[rr][cc]
                    #print("temp = ", temp)
                validSet.add(temp)
                #print("len(validSet) = {0} / validSet = {1}".format(len(validSet), validSet))
            if len(validSet) == rowSize:
                unique_index.append(c)
                print("result = ", unique_index)

        delSet = set()
        for stdMinElem in unique_index:
            print("stdMinElem = ", stdMinElem)
            for idx, compMinElem in enumerate(unique_index):
                print("<enumerate(unique_index)> idx = {0} / compMinElem = {1}".format(idx, compMinElem))
                if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                    delSet.add(unique_index.index(compMinElem))
        answer = len(unique_index) - len(delSet)
    return answer


relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]
print(solution2(relation))
