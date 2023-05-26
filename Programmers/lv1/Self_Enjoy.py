def solution(cards):
    answer = 0
    counts = []

    cards = [0] + cards
    print("1. cards = ", cards)
    N = len(cards)

    for i in range(1, N):
        # 열려 있는 상자
        print("2. cards[{0}] = {1}".format(i, cards[i]))
        if not cards[i]:
            continue
        # 그룹 상자의 수
        count = -1
        #print("3. cards[{0}] = {1}".format(i, cards[i]))
        print("3. (else) count = ", count)
        while i:
            count += 1
            print("4. (while) count = ", count)
            cards[i], i = 0, cards[i] # 상자 오픈한 후 다음 상자
            print("5. cards[{0}], i({0}) = 0, cards[{0}] >> {1}".format(i, cards[i]))
        counts.append(count)
        print("6. counts.append({0}) = {1}".format(count, counts))
    # 1번 상자 그룹을 제외하고, 남는 상자가 없을 때 게임 종료
    if len(counts) < 2:
        return 0

    # 게임 점수 >>> 1번 그룹의 상자 수 * 2번 그룹의 상자 수
    counts.sort()
    answer = counts[-1] * counts[-2]
    return answer

cards = [8, 6, 3, 7, 2, 5, 1, 4]
print(solution(cards))