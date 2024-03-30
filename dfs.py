def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(graph[vertex] - visited)

    return path

graph = {
    1: {3},
    2: {4},
    3: {1},
    4: {2}
}
start_vertex = 1
print(dfs(graph, start_vertex))  
