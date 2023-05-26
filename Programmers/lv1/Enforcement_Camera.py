def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    print("routes = {0}".format(routes))
    leng = len(routes)
    print("leng = {0}".format(leng))
    checked = [0] * leng
    print("checked = {0}".format(checked))

    for i in range(leng):
        if checked[i] == 0:
            camera = routes[i][1] # 진출 지점 카메라 갱신
            answer += 1
            print("1. if checked[{0}] == 0: ".format(i))
            print(">>> camera = {0}, answer = {1}".format(camera, answer))
        for j in range(i + 1, leng):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
                print("2. if routes[{0}][0]:{2} <= camera:{1} <= routes[{0}][1]:{3} and checked[{0}]:{4}".format(j, camera, routes[j][0], routes[j][1], checked[j]))
    return answer

def solution2(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])

    camera = -30001

    for route in routes:
        print("route = {0}".format(route))
        if camera < route[0]:
            print("camera:{0} < route[0]:{1}".format(camera, route))
            answer += 1
            print("answer = {0}".format(answer))
            camera = route[1]
            print("camera = {0}".format(camera))
    return answer

routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
print(solution2(routes))