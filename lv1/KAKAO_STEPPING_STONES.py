def solution(stones, k):
    answer = 0
    while(True):
        answer += 1
        print("1. answer = ", answer)
        for i in range(len(stones)):
            #print("<check> i = {0}, len(stones) = {1}".format(i, len(stones)))
            print("2. i = {0}, stones[{0}] = {1}".format(i, stones[i]))
            if stones[i] == 0:
                print("2-1. continue")
                continue
            else:
                stones[i] -= 1
                print("2-2. stones[{0}] -= 1 >>> {1}".format(i, stones[i]))
        count = 0
        for stone in stones:
            print("3. stone = {0}".format(stone))
            if stone == 0:
                count += 1
                print("3-1. count = {0}".format(count))
                if count == k:
                    print("4. count:{0} == k:{1}".format(count, k))
                    return answer
            else:
                print("3-2. count = 0")
                count = 0

def solution2(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        # print("1. temp = {0}".format(temp))
        mid = (left + right) // 2
        # print("2. mid = (left+right)//2")
        # print(">>> mid = ({0} + {1}) // 2 >>> {2}".format(left, right, mid))
        cnt = 0
        for t in temp:
            # print("3. t = {0} / temp = {1}".format(t, temp))
            if t - mid <= 0:
                # print("3-1. t:{0} - mid:{1} === {2} <= 0".format(t, mid, t - mid))
                cnt += 1
                # print("3-1. cnt = {0}".format(cnt))
            else:
                cnt = 0
                # print("3-2. cnt = {0}".format(cnt))
            if cnt >= k:
                # print('=== 3-3. cnt >= k // break ===')
                break
        if cnt >= k:
            # print("4. cnt:{0} >= k:{1}".format(cnt, k))
            right = mid - 1
            # print("4-1. right = mid:{0} - 1 == {1}".format(mid, right))
        else:
            left = mid + 1
            # print("5. left = mid:{0} + 1 == {1}".format(mid, left))

    return left

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution2(stones, k))