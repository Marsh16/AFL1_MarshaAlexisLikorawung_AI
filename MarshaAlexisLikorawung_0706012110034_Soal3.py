# Fungsi pencarian jalur menggunakan metode DFS (Depth-First Search).
def depth_first_search(graph, start, end):
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

# mulai program
if __name__ == "__main__":
# Definisi graf berisi keterhubungan antar lokasi.
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

 # Identifikasi node dengan nama yang berbeda. agar bisa kalau dipanggil tetap gianyar bukan gianyar_1 atau gianyar_2
    node_identifiers = {
        "gianyar": "gianyar_1",
        "gianyar": "gianyar_2"
    }

 # Fungsi untuk memperbarui isi dari yang gianyar_1 atau gianyar_2 jadi gianyar aja, dari setiap node berdasarkan identifikasi gianyar.
    def update_neighbors():
        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                if neighbor in node_identifiers:
                    neighbors[node_identifiers[neighbor]] = weight
                    del neighbors[neighbor]

# Memanggil fungsi untuk memperbarui isi.
    update_neighbors()

# Meminta input untuk node awal dan akhir. dan ada error handlingnya kalau tidak sesuai graph 
    while True:
        start_node = input("Input the start node: ")
        if start_node == 'gianyar':
            start_node = 'gianyar_2'
            break
        elif start_node in graph:
            break
        else:
            print(f"'{start_node}' is not a valid node. Please try again.")

    while True:
        end_node = input("Input the end node: ")
        if end_node in graph:
            # Mencari jalur jika tujuan akhir adalah 'gianyar'. maka, gianyar 1 2nya harus diconvert jadi gianyar saja dan cek kedua dfsnya untuk yang gianyar1 dan dfs gianyar2, kemudian jika yang ditemukan gianyar 1 yang di print tetap gianyar dan jika ditemukan gianyar 2 juga diprint tetap gianyar
            result = depth_first_search(graph, start_node, end_node)
            if result:
                result = [node.replace("gianyar_1", "gianyar").replace("gianyar_2", "gianyar") for node in result]
                print(f"The path from {start_node} to {end_node} is: {' -> '.join(result)}")
                break
            else:
                print(f"No path found from {start_node} to {end_node}")
                break
        elif end_node == 'gianyar':
            result_1 = depth_first_search(graph, start_node, "gianyar_1")
            result_2 = depth_first_search(graph, start_node, "gianyar_2")

            if result_1:
                result_1 = [node.replace("gianyar_1", "gianyar") for node in result_1]
                print(f"The path from {start_node} to gianyar is: {' -> '.join(result_1)}")
                break
            elif result_2:
                result_2 = [node.replace("gianyar_2", "gianyar") for node in result_2]
                print(f"The path from {start_node} to gianyar is: {' -> '.join(result_2)}")
                break
            else:
                print(f"No path found from {start_node} to gianyar")
                break
        else:
            print(f"'{end_node}' is not a valid node. Please try again.")
