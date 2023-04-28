def solution(new_id):
    # 1단계(전체 소문자)
    new_id = new_id.lower()

    # 2단계(-_' 제외한 특수문자 다 제거)
    answer = ''
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i

    # 3단계(..., .. 을 .으로 치환)
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계(. 가 처음이나 끝에 위치하면 제거)
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    # 5단계(공백이 있으면 'a'로 치환)
    answer = 'a' if answer == '' else answer

    # 6단계(16자 이상일 시 15개의 문자 제외하고 나머진 삭제
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계(2자 이하일 시 마지막 문자를 길이가 3이상 될 때까지 반복해서 붙임)
    while len(answer) < 3:
        answer += answer[-1]

    return answer



new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))