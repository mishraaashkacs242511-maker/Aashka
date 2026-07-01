from collections import deque
import time

# Graph
mumbai_map = {
    'Lokhandwala': ['Oshiwara Link Road', 'Yari Road', 'Veera Desai Road'],
    # Route 1
    'Oshiwara Link Road': ['Oshiwara'],
    'Oshiwara': ['SV Road'],
    'SV Road': ['Juhu Circle'],
    'Juhu Circle': ['Juhu'],
    # Route 2
    'Yari Road': ['Versova'],
    'Versova': ['Seven Bungalows'],
    'Seven Bungalows': ['Juhu Tara Road'],
    'Juhu Tara Road': ['Juhu'],
    # Route 3
    'Veera Desai Road': ['Andheri Link Road'],
    'Andheri Link Road': ['JP Road'],
    'JP Road': ['DN Nagar'],
    'DN Nagar': ['Juhu'],
    # Destination
    'Juhu': []
}

# BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    nodes = 0
    while queue:
        path = queue.popleft()
        node = path[-1]
        nodes += 1
        if node == goal:
            return path, nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

# DFS (iterative)
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    nodes = 0
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        nodes += 1
        if node == goal:
            return path, nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(path + [neighbor])

# Run
start, goal = "Lokhandwala", "Juhu"

t0 = time.perf_counter()
bfs_path, bfs_nodes = bfs(mumbai_map, start, goal)
t1 = time.perf_counter()

t2 = time.perf_counter()
dfs_path, dfs_nodes = dfs(mumbai_map, start, goal)
t3 = time.perf_counter()

# Results
print("BFS:", " -> ".join(bfs_path))
print("Steps:", len(bfs_path)-1, "| Nodes visited:", bfs_nodes, "| Time:", t1-t0)

print("\nDFS:", " -> ".join(dfs_path))
print("Steps:", len(dfs_path)-1, "| Nodes visited:", dfs_nodes, "| Time:", t3-t2)

print("\nComparison")
print("Shorter path:", "BFS" if len(bfs_path) < len(dfs_path) else "DFS" if len(dfs_path) < len(bfs_path) else "Equal")
print("Fewer nodes visited:", "BFS" if bfs_nodes < dfs_nodes else "DFS" if dfs_nodes < bfs_nodes else "Equal")
print("\nTime Complexity: O(V + E) for both")
print("Space Complexity: O(V) for both")
