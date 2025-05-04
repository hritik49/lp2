def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# ------- User Input Part --------
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(1, n+1)}

for _ in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)  # For undirected graph

start = int(input("Enter start node: "))

print("\nDFS Traversal:")
dfs([], graph, start)

print("\nBFS Traversal:")
bfs([], graph, start)