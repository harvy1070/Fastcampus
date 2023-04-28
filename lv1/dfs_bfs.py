graph_list = {1:set([3, 4]),
              2:set([3, 4, 5]),
              3:set([1, 5]),
              4:set([1]),
              5:set([2, 6]),
              6:set([3, 5])
              }
root_node = 1

from collections import deque

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        print("1. while queue = ", queue)
        n = queue.popleft()
        print("2. n = ", n)
        if n not in visited:
            visited.append(n)
            print("3. **** n not in visited ****")
            print(">>> {0} not in {1}".format(n, visited))
            queue += graph[n] - set(visited)
            print("4. **** queue += graph[n] - set(visited) ****")
            print(">>> queue = {0} + graph[{1}]:{2} - set({3}):{4}".format(queue, n, graph[n], visited, set(visited)))
    return visited

def dfs(graph, root):
    visited = []
    stack = [root]
    while stack:
        print("1. while = {0}".format(stack))
        n = stack.pop()
        print("2. n = ", n)
        if n not in visited:
            print("3. {0} not in visited = {1}".format(n, visited))
            visited.append(n)
            print("4. visited = {0}".format(visited))
            stack += graph[n] - set(visited)
            print("5. stack += graph[n] - set(visited)")
            print(">>> stack += {0} - {1}".format(graph[n], set(visited)))
    return visited

#print(bfs(graph_list, root_node))
print(dfs(graph_list, root_node))