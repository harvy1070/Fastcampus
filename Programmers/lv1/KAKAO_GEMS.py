def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))  # 보석 종류 갯수
    left, right = 0, 0  # left는 보석 빼 줄 포인터, right는 보석 더해 줄 포인터
    gem_dict = {gems[0]: 1}
    print("1. gem_dict = {0}".format(gem_dict))

    while left < len(gems) and right < len(gems):  # 투 포인터가 범위를 벗어나면 무한루프 종료
        print("2. left = {0} < len(gems) = {1} and right = {2} < len(gems) = {1}".format(left, len(gems), right))
        # 딕셔너리에 보석 종류가 다 들어오는 경우
        if len(gem_dict) == size:
            print("3. len(gem_dict):{0}, size:{1}".format(len(gem_dict), size))
            if right - left < answer[1] - answer[0]:  # 최소 크기 확인
                print("4. right:{0} - left:{1} < answer[1]:{2} - answer[0]:{3}".format(right, left, answer[1], answer[0]))
                answer = [left, right]
                print("5. answer:{2} = [left:{0}, right:{1}".format(left, right, answer))
            else:
                gem_dict[gems[left]] -= 1
                print("6. gem_dict[gems[left]] -= 1")
                print(">>> gem_dict[{0}] = gem_dict[{0}]:{1} - 1".format(gems[left], gem_dict[gems[left]]))
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]  # count가 0이 되면 key가 없어야하므로 반드시 del
                left += 1
                print("7. left = {0}".format(left))
        # 다 들어오지 않는 경우
        else:
            right += 1
            print("8. right = {0} / len(gems) = {1}".format(right, len(gems)))
            if right == len(gems):
                print(" ============== break =============")
                break

            if gems[right] in gem_dict:  # 딕셔너리 key에 있으면 count
                gem_dict[gems[right]] += 1
                print("9. <if> gem_dict[gems[right]] += 1")
                print(">>> gem_dict[{0}] = {1}".format(gems[right], gem_dict[gems[right]]))

            else:  # 없으면 추가
                gem_dict[gems[right]] = 1
                print("10. <else> gem_dict[gems[right]] = 1")
                print(">>> gem_dict[{0}] = {1}".format(gems[right], gem_dict[gems[right]]))

    return [answer[0] + 1, answer[1] + 1]  # 시작 인덱스가 1번 진열대 부터 라서 1 증가

gems = ["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]
print(solution(gems))