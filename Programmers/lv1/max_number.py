# time over(fail)
# from itertools import combinations
# def solution(number, k):
#     answer = sorted(list(combinations(list(number), len(number) - k)), reverse = True)
#     return ''.join(answer[0])

# stack 활용
# def solution(number, k):
#     answer = []
#     for num in number:
#         print("(number)num = ", num)
#         if not answer:
#             answer.append(num)
#             print("1. (not answer append)answer = ", answer)
#             continue
#         if k > 0:
#             while answer[-1] < num:
#                 print("answer[-1] = ", answer[-1])
#                 print("2. (pop)answer = ", answer)
#                 answer.pop()
#                 k -= 1
#                 print("(counting)k = ", k)
#                 if not answer or k <= 0:
#                     break
#         answer.append(num)
#         print("3. (append)answer = ", answer)
#     answer = answer[:-k] if k > 0 else answer
#     return ''.join(answer)

# stack 활용
def solution(number, k):
    stack = [number[0]]
    print("1. stack = ", stack)
    for num in number[1:]:
        print("2. num = ", num)
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
            print("3. (pop)stack = ", stack)
        stack.append(num)
        print("4. (append)stack = ", stack)
    if k != 0:
        stack = stack[:-k]
        print("5. (reverse)stack = ", stack)
    return ''.join(stack)

number = "654321"
k = 1
print(solution(number, k))