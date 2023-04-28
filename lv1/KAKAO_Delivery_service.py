import datetime
def solution(a, b):
    answer = ''
    now = datetime.datetime(2016, a, b)
    print(now)
    answer = now.strftime("%a")
    return answer.upper()

a = 5
b = 24
print(solution(a, b))