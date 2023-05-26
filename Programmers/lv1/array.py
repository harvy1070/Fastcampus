# 선택정렬
def select_array(array):
    for i in range(len(array)):
        min_index = i
        #print("min_index = ", min_index)
        for j in range(i+1, len(array)):
            #print("j = ", j)
            if array[min_index] > array[j]:
                min_index = j
                #print("(if)min_index = ", min_index)
        array[i], array[min_index] = array[min_index], array[i]
        #print("swap = ", array[i], array[min_index])
    print(array)

# 삽입정렬
def insert_array(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print(array)

# 퀵정렬
def quick_sort1(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort1(array, start, right-1)
    quick_sort1(array, right+1, end)

def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

# 계수정렬
def calc_array(array2):
    count = [0] * (max(array2) + 1)
    for i in range(len(array2)):
        count[array2[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(calc_array(array2))
#print(quick_sort2(array))
#print(select_array(array))
#print(insert_array(array))
#quick_sort1(array, 0, len(array)-1)
#print(array)