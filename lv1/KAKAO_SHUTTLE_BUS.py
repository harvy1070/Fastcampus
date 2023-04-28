def solution(n, t, m, timetable):
    answer = 0
    crewtime = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    print("1. crewtime = {0}".format(crewtime))
    crewtime.sort()

    bustime = [9*60 + t * i for i in range(n)]
    print("2. bustime = {0}".format(bustime))

    i = 0
    for tm in bustime:
        print("<for> 3. tm = {0}".format(tm))
        cnt = 0
        while cnt < m and i < len(crewtime) and crewtime[i] <= tm:
            print("<for/while> 4. cnt < m and i < len(crewtime) and crewtime[i] <= tm:")
            print(">>> {0} < {1} and {2} < {3} and {4} <= {5}".format(cnt, m, i, len(crewtime), crewtime[i], tm))
            i += 1
            cnt += 1
            print("<for/while> 5. i = {0}, cnt = {1}".format(i, cnt))
        if cnt < m:
            answer = tm
            print("<for/if> cnt:{0} < m:{1} == answer = tm:{2}".format(cnt, m, tm))
        else:
            answer = crewtime[i - 1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

#n = 셔틀 운행 횟수 / t = 배차 간격 / m = 셔틀에 탈 수 있는 크루원 수 / timetable = 크루원 도착 시각
n, t, m = 2, 10, 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))
