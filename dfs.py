def dfs_with_length_and_path(graph, start, end): #Алгоритм поиска в глубину
    if start not in graph or end not in graph:
        raise ValueError("Invalid start or end vertex")

    visited = set()
    stack = [(start, 0, [start])]  

    while stack:
        vertex, length, path = stack.pop()
        if vertex == end:
            return length, path  
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]  
                    stack.append((neighbor, length + 1, new_path))

    return -1, []

graph = { #граф для алгоритма
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
start_vertex = 1
end_vertex = 4

try: #попытка использования алгоритма
    length, path = dfs_with_length_and_path(graph, start_vertex, end_vertex)
    print("Length of the shortest path:", length)
    print("Shortest path:", path)
except ValueError as e:
    print("Error:", e)
