# Queen을 배열에 배치한 후 check함수로 넘겨서 위치가 적합한지 체크
def n_queen(n, x, queen):
    result = 0
    if x == n:
        return 1

    for i in range(n):
        queen[x] = i
        print("<n_queen> 1. queen[{0}] = {1}".format(x, i))
        print("<n_queen> 2. x = {0}, {1}".format(x, queen))
        if check(x, queen):
            result += n_queen(n, x+1, queen)
            print("<n_queen> 3. result += n_queen({0}, {1}, {2}) // {3}".format(n, x+1, queen, result))
    return result

# n_queen 함수에서 받아온 Queen의 위치가 가로 / 세로상, 대각선에 중복되어 있는지의 여부를 확인
def check(x, queen):
    for i in range(x):
        print("<check> 1.x = {0}, i = {1}".format(x, i))
        # queen[x]와 queen[i]를 가로, 세로상으로 비교한 후 abs를 활용하여 대각선 위치 체크
        if queen[x] == queen[i] or abs(x-i) == abs(queen[x] - queen[i]):
            print("<check> 2-1. queen[{0}] == queen[{1}] or abs({0}-{1}) == abs(queen[{0}]-queen[{1}])".format(x, i))
            print("<check> 2-2. {0} == {1} or {2} == {3}".format(queen[x], queen[i], abs(x-i), abs(queen[x]-queen[i])))
            return False
    return True

def solution(n):
    queen = [0] * n
    print("<solution> 1. queen = ", queen)
    answer = n_queen(n, 0, queen)

    return answer


def dfs(queen, n, row):
    count = 0

    if n == row:
        return 1
    # 가로 진행
    for col in range(n):
        queen[row] = col
        print("queen[{0}] = {1}".format(row, col))
        # 세로 진행
        for x in range(row):
            print()
            if queen[x] == queen[row]:
                break
            # 대각선 진행
            if abs(queen[x] - queen[row]) == (row-x):
                break
        else:
            count += dfs(queen, n, row+1)

    return count

def solution2(n):
    queen = [0] * n
    return dfs(queen, n, 0)

n = 4
print(solution2(n))