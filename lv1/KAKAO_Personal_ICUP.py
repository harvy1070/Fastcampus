def datetoday(date):
    year, month, day = map(int, date.split("."))
    print(year, month, day)
    return (year * 12 * 28) + (month * 28) + day
def solution(today, terms, privacies):
    answer = []
    # today를 총 일수로 변환
    today = datetoday(today)

    # terms의 개월 수를 총 일수로 변환하여 주어진 약관에 맞게 매칭(dict)
    terms_info = dict()
    for term in terms:
        term = term.split()
        terms_info[term[0]] = int(term[1]) * 28

    # privacies의 값 중 약관 표기값을 제외한 일자만 추출하여 datetoday함수로 변환
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if datetoday(date) + terms_info[term] <= today:
            answer.append(i+1)
    # print(datetoday(date), terms_info, today)

    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))