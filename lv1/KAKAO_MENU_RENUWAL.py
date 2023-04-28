# combinations와 Counter 사용1
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        c_array = []
        #print("1. c = ", c)
        for o in orders:
            #print("2. o = ", o)
            c_array += list(combinations(sorted(o), c))
            #print("3. (combinations)c_array = ", c_array)
        c_array = Counter(c_array)
        #print("4. (Counter)c_array = ", c_array)
        answer += [''.join(k) for k, v in c_array.items() if v == max(c_array.values()) and v > 1]
        #print("5. (key, values)answer = ", answer)
    #print("6. sorted(answer) = ", sorted(answer))
    return sorted(answer)

# combinations와 Counter 사용 2
def solution2(orders, course):
    answer = []
    for c in course:
        temp = []
        for o in orders:
            comb = combinations(sorted(o), c)
            temp += comb

        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)

def solution3(orders, course):
    result = []

    for course_size in course:
        order_combination = []
        print("1. (1번 for문)order_combination = ", order_combination)
        for order in orders:
            order_combination += combinations(sorted(order), course_size)
            print("2. (2번 for문)order_combination = ", order_combination)

        most_ordered = Counter(order_combination).most_common()
        print("3. most_ordered = ", most_ordered)
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
        print("4. result = ", result)
    return [''.join(v) for v in sorted(result)]

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution3(orders, course))