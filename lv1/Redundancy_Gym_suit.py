# def solution(n, lost, reserve):
#     set_reserve = set(reserve) - set(lost)
#     set_lost = set(lost) - set(reserve)
#     print(set_reserve, set_lost)
#     for i in set_reserve:
#         if i - 1 in set_lost:
#             set_lost.remove(i-1)
#             # print(i)
#             # print("i - 1 = set_lost:{0}".format(set_lost))
#         elif i + 1 in set_lost:
#             set_lost.remove(i+1)
#             print(i)
#             # print("i - 1 = set_lost:{0}".format(set_lost))
#     return n-len(set_lost)

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    # print(_reserve, _lost)
    for r in _reserve:
        f = r - 1
        b = r + 1
        print(f, b)
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)


n = 5
lost = [2, 4, 5, 1]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))