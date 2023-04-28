import math
def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    print("1. m = ", m)
    for mi in musicinfos:
        print("2. mi = ", mi)
        start, end, title, code = mi.split(",")

        print("3. start = {0} / end = {1} / title = {2} / code = {3}".format(start, end, title, code))
        hour, minute = map(int, start.split(":"))
        print("4. <start>hour = {0} / minute = {1}".format(hour, minute))
        start = hour * 60 + minute
        print("5. start = ", start)

        hour, minute = map(int, end.split(":"))
        print("6. <end> hour = {0} / minute = {1}".format(hour, minute))
        end = hour * 60 + minute
        print("7. end = ", end)
        duration = end - start
        print("8. duration = ", duration)

        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        print("9. code = ", code)
        code *= math.ceil(duration / len(code))
        print("10. code(math.ceil(duration / len(code)) = ", code)
        code = code[:duration]
        print("11. code[:duration] = ", code)
        if m not in code:
            continue

        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
            answer = (duration, start, title)
            print("12. duration = {0} / start = {1} / title = {2} / (sum)answer = {3}".format(duration, start, title, answer))

    if answer:
        print("13. answer[-1]", answer[-1])
        return answer[-1]

    return "(None)"

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))