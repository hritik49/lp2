import heapq

def prim_mst(user_graph, vertices):
    visited = [False] * vertices
    min_heap = [(0, 0)]  # (weight, start_vertex)
    total_weight = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        for v, w in user_graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return total_weight

# ---------------------------
# Main Program Starts Here
# ---------------------------
if __name__ == "__main__":
    print("Prim's Minimum Spanning Tree Algorithm")
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    # Create adjacency list
    graph = [[] for _ in range(V)]

    print("Enter edges in the format: u v weight")
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))  # Since the graph is undirected

    mst_weight = prim_mst(graph, V)
    print("Total weight of the Minimum Spanning Tree is:", mst_weight)