from itertools import combinations

def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num // 2) + 1):
            if num % n == 0:
                return False
        return True

def is_prime2(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    cnt = list(combinations(nums, 3))
    for i in cnt:
        if is_prime2(sum(i)):
            answer += 1
    return answer

nums = [1, 2, 7, 6, 4]
print(solution(nums))