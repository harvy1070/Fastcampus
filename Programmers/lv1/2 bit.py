def solution(numbers):
    answer = []

    for n in numbers:
        bin_n = list('0' + bin(n)[2:])
        print("1. bin_n = ", bin_n)
        idx = ''.join(bin_n).rfind('0')
        print("2. idx = ", idx)
        bin_n[idx] = '1'
        print("3. bin_n[idx] = ", bin_n[idx])

        if n % 2 == 1:
            bin_n[idx+1] = '0'
            print("4. (if) n = ", n)
        answer.append(int(''.join(bin_n), 2))
        print("5. answer = ", answer)
    return answer

numbers = [2, 7]
print(solution(numbers))