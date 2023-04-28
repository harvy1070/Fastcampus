def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                a.append(i)
                b.append(j)
                print(a, b)
    return [min(a), min(b), max(a)+1, max(b)+1]

def solution2(wallpaper):
    answer = [51, 51, 0, 0]
    lux, luy, rdx, rdy = 0, 1, 2, 3

    for i, elements in enumerate(wallpaper):
        for j, element in enumerate(elements):
            print()
            if element == '#':
                answer[lux] = min(answer[lux], i)
                answer[luy] = min(answer[luy], j)
                answer[rdx] = max(answer[rdx], i+1)
                answer[rdy] = max(answer[rdy], j+1)
    return answer

wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))