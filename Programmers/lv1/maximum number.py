def solution(numbers):
    numbers = list(map(str, numbers))
    print("1. (list)numbers = ", numbers)
    numbers.sort(key=lambda x:x*3, reverse=True)
    print("2. (sort)numbers = ", numbers)
    return str(int(''.join(numbers)))

numbers = [3, 30, 34, 5 ,9]
print(solution(numbers))
