def dfs(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    if start == end:
        return [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs(graph, neighbor, end, visited)
            if path:
                return [start] + path

    return None

if __name__ == "__main__":
    graph_data = [
        ("denpasar", "mengwi"),
        ("mengwi", "canggu"),
        ("mengwi", "sukawati"),
        ("sukawati", "tegalang"),
        ("sukawati", "bangli"),
        ("mengwi", "tabanan"),
        ("denpasar", "ngerebong"),
        ("ngerebong", "kintamani"),
        ("kintamani", "padangbai"),
        ("ngerebong", "abiansemal"),
        ("abiansemal", "gianyar"),
        ("gianyar", "padangbai"),
        ("abiansemal", "gianyar"),
        ("gianyar", "padangbai"),
        ("ngerebong", "gianyar")
    ]

    graph = {}
    for edge in graph_data:
        if edge[0] not in graph:
            graph[edge[0]] = {}
        graph[edge[0]][edge[1]] = 1

    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")
    result = dfs(graph, start_node, end_node)

    if result:
        print(f"The path from {start_node} to {end_node} is: {' -> '.join(result)}")
    else:
        print(f"No path found from {start_node} to {end_node}")

