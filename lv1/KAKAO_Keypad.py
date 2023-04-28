def solution(numbers, hand):
    answer = ''
    # 키패드 좌표 설정
    dic = {1:[0,0], 2:[0,1], 3:[0,2],
           4:[1,0], 5:[1,1], 6:[1,2],
           7:[2,0], 8:[2,1], 9:[2,2],
           '*':[3,0], 0:[3,1], '#':[3,2]}

    # 시작 위치
    left_h = dic['*']
    right_h = dic['#']

    for i in numbers:
        now = dic[i]

        if i in [1, 4, 7]:
            answer += 'L'
            left_h = now
        elif i in [3, 6, 9]:
            answer += 'R'
            right_h = now
        else:
            ld, rd = 0, 0
            # 좌표 거리 계산
            for a, b, c in zip(left_h, right_h, now):
                ld += abs(a - c)
                rd += abs(b - c)

            # 왼손이 가까운 경우
            if ld < rd:
                answer += 'L'
                left_h = now
            # 오른손이 가까운 경우
            elif ld > rd:
                answer += 'R'
                right_h = now
            # 두 거리가 같은 경우
            else:
                if hand == 'left':
                    answer += 'L'
                    left_h = now
                else:
                    answer += 'R'
                    right_h = now
    return answer




numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
