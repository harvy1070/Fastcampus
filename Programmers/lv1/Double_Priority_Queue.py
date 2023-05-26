import heapq

def solution(operations):
    heap = []
    max_heap = []

    for o in operations:
        current = o.split()
        print("o.split = {0}".format(o.split()))
        if current[0] == 'I':
            print("====================if======================")
            print("<if> current[0] = {0}".format(current[0]))
            num = int(current[1])
            print("<current[0] == 'I'> num >>> {0}".format(num))
            heapq.heappush(heap, num)
            print(">>> heapq(heap) = {0}".format(num))
            heapq.heappush(max_heap, (num*-1, num))
            print(">>> heapq(max_heap) = {0}".format(num*-1, num))
            print("====================if======================")
        else:
            print("===================else=====================")
            print("<else> current[0] = {0}".format(current[0]))
            print("<else> heap = {0}, max_heap = {1}".format(heap, max_heap))
            if len(heap) == 0:
                pass
            elif current[1] == '1':
                print("******** current[1] == 1 ********")
                max_value = heapq.heappop(max_heap)[1]
                print("<else> max_value = {0}".format(max_value))
                heap.remove(max_value)
                print("<else> heap = {0}".format(heap))
            elif current[1] == '-1':
                print("******** current[1] == -1 ********")
                min_value = heapq.heappop(heap)
                print("<else> min_value = {0}".format(min_value))
                max_heap.remove((min_value * -1, min_value))
                print("<else> max_heap = {0}".format(max_heap))
                print(">>> {0}".format((min_value * -1, min_value)))
            print("===================else=====================")

    if heap:
        print("******************* result *******************")
        print("{0}".format([heapq.heappop(max_heap)[1], heapq.heappop(heap)]))
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        print("******************* result *******************")
        print("[0, 0]")
        print("******************* result *******************")
        return [0, 0]

operations = ["I 16",
              "I -5643",
              "D -1",
              "D 1",
              "D 1",
              "I 123",
              "D -1"]
print(solution(operations))