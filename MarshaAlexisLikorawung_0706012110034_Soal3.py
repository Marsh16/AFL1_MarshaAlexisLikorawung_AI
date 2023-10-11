def dfs(graph, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (node, path) = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if node == end:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None

def print_graph_tree(graph, node, depth=0):
    print("  " * depth + node)
    for neighbor, _ in graph.get(node, {}).items():
        print_graph_tree(graph, neighbor, depth + 1)

if __name__ == "__main__":
    graph = {
        "denpasar": {"mengwi": 1, "ngerebong": 1},
        "mengwi": {"canggu": 1, "sukawati": 1, "tabanan": 1},
        "canggu": {},
        "sukawati": {"tegalang": 1, "bangli": 1},
        "tegalang": {},
        "bangli": {},
        "tabanan": {},
        "ngerebong": {"kintamani": 1, "abiansemal": 1, "gianyar_1": 1},
        "kintamani": {"padangbai": 1},
        "abiansemal": {"gianyar_2": 2},
        "gianyar_2": {"padangbai": 1},
        "padangbai": {},
        "gianyar_1": {},
    }

    node_identifiers = {
        "gianyar": "gianyar_1",
        "gianyar": "gianyar_2"
    }

    print_graph_tree(graph, "denpasar")

    # Replace "gianyar" with the corresponding identifier
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            if neighbor in node_identifiers:
                neighbors[node_identifiers[neighbor]] = weight
                del neighbors[neighbor]

    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")
    if end_node == 'gianyar':
        result_1 = dfs(graph, start_node, "gianyar_1")
        result_2 = dfs(graph, start_node, "gianyar_2")

        if result_1:
            result_1 = [node.replace("gianyar_1", "gianyar") for node in result_1]
            print(f"The path from {start_node} to gianyar_1 is: {' -> '.join(result_1)}")
        elif result_2:
            result_2 = [node.replace("gianyar_2", "gianyar") for node in result_2]
            print(f"The path from {start_node} to gianyar_2 is: {' -> '.join(result_2)}")
        else:
            print(f"No path found from {start_node} to gianyar")

    else:
        result = dfs(graph, start_node, end_node)

        if result:
            result = [node.replace("gianyar_1", "gianyar").replace("gianyar_2", "gianyar") for node in result]
            print(f"The path from {start_node} to {end_node} is: {' -> '.join(result)}")
        else:
            print(f"No path found from {start_node} to {end_node}")





