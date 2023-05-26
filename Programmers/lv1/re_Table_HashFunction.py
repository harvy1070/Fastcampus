import functools

def sortByCondition(data, col):
    print("2) <sortByCondition> 1. data = {0}, col = {1}".format(data, col))
    def compare(row1, row2):
        print("3) <compare> 1. row1 = {0}, 2. row2 = {1}".format(row1, row2))
        if row1[col] == row2[col]:
            print("3) <compare> 2. if row1[col] == row2[col]")
            print(">>> row1[{0}] = {1} / row2[{0}] = {2}".format(col, row1[col], row2[col]))
            print("3) <compare> 3. return row2[0] - row1[0]")
            print(">>> return {0} - {1}".format(row2[0], row1[0]))
            return row2[0] - row1[0]
        print("3) <compare> 4. return row1[col] - row2[col]")
        print(">>> return row1[{0}] = {1} - row2[{0}] = {2}".format(col, row1[col], row2[col]))
        return row1[col] - row2[col]
    print("*****  3) <compare> sorted >>> {0}  *****".format(sorted(data, key=functools.cmp_to_key(compare))))
    return sorted(data, key = functools.cmp_to_key(compare))

def calculateSValue(datum, row):
    value = 0
    for col in datum:
        value += col % (row+1)
    return value

def calculateHash(data, row_begin, row_end):
    hash_value = 0
    for row in range(row_begin, row_end + 1):
        datum = data[row]
        hash_value ^= calculateSValue(datum, row)
    return hash_value

def solution(data, col, row_begin, row_end):
    data = sortByCondition(data, col-1)
    print("1) <solution> 1. data = {0}".format(data))
    return calculateHash(data, row_begin-1, row_end-1)

data = [
    [2, 2, 6],
    [1, 5, 10],
    [4, 2, 9],
    [3, 8, 3]
]
col = 2
row_begin = 2
row_end = 3
print(solution(data, col, row_begin, row_end))