def solution(n, arr1, arr2):
    fin_list = []
    for i, j in zip(arr1, arr2):
        list1 = int(bin(i)[2:])
        list2 = int(bin(j)[2:])
        # print(list1, list2)
        fin_list.append(str(list1+list2).zfill(n))
        # print(fin_list)
    fin = []
    for fin_l in fin_list:
        fin_r = ''
        for f in fin_l:
            if f == '0':
                fin_r += " "
            else:
                fin_r += "#"
        print(fin_l)
        fin.append(fin_r)
    return fin

n = 5
arr1 = [9, 10, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))