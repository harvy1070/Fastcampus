from itertools import permutations
def check(user, ban):
    print("<check> 1. user = {0}, ban = {1}".format(user, ban))
    if len(user) != len(ban):
        return False
    else:
        for i, j in zip(user, ban):
            print("<check> 2. i = {0}, j = {1}".format(i, j))
            if j == '*':
                continue
            if i != j:
                return False
        return True

def solution(user_id, banned_id):
    answer = []

    for i in permutations(user_id, len(banned_id)):
        print("<solution> 1. i = {0}".format(i))
        count = 0
        for a, b in zip(i, banned_id):
            print("<solution> 2. a = {0}, b = {1}".format(a, b))
            if check(a, b):
                count += 1
                print("<solution> 3. count = {0}".format(count))
        if count == len(banned_id):
            print("<solution> 4. count:{0} == len(banned_id):{1} >>> ".format(count, len(banned_id)))
            if set(i) not in answer:
                print("<solution> 5. set({0}):{1} not in answer:{2} >>> ".format(i, set(i), answer))
                answer.append(set(i))
                print("<solution> 6. answer = {0}".format(answer))

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

print(solution(user_id, banned_id))

