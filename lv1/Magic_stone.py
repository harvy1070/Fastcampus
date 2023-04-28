def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        print("1. remainder({1}) = storey({0}) % 10".format(storey, remainder))
        # 6 - 9
        if remainder > 5:
            answer += (10 - remainder)
            print("2. (remainder > 5) >>> answer({0}) += (10- remainder({1})".format(answer, remainder))
            storey += 10
            print("3. (remainder > 5) >>> storey = ", storey)

        elif remainder < 5:
            answer += remainder
            print("4. (remainder < 5) >>> answer({0}) = {1}".format(answer, remainder))

        else:
            if (storey // 10) % 10 > 4:
                print("5. (else) >>> // (storey({0}) // 10) % 10 > 4 //".format(storey))
                storey += 10
                print("6. (else) >>> // (storey({0}) // 10) % 10 > 4 //".format(storey))
            answer += remainder
            print("7. (else) >>> answer({0}) += remainder({1})".format(answer, remainder))
        storey //= 10
        print("8. storey //= 10 >>> {0}".format(storey))
    return answer

def solution2(storey):
    print("1. if storey < 10: >>> min(storey, 11 - storey")
    print(">>> if {0} < 10: >>> min({0}, 11 - {0})".format(storey))
    if storey < 10:
        return min(storey, 11 - storey)
    left = storey % 10
    print("2. left = storey % 10")
    print(">>> {0} = {1} % 10".format(left, storey))
    print("3. min(left + solution2(storey // 10), 10 - left + solution2(storey // 10 + 1")
    print(">>> min({0} + solution2({1} // 10), 10 - {0} + solution2({1} // 10 + 1".format(left, storey))
    return min(left + solution2(storey // 10), 10 - left + solution2(storey // 10 + 1))

storey = 2554
print(solution2(storey))