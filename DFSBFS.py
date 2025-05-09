# Input the graph
graph = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ").strip()
    neighbors = input(f"Enter neighbors of {node} (space separated): ").strip().split()
    graph[node] = neighbors
print(graph)

# DFS function
def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS function
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Menu
while True:
    print("\nMenu:")
    print("1. BFS")
    print("2. DFS")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        start = input("Enter starting node: ")
        print("BFS Traversal:")
        bfs(graph, start)
    elif choice == '2':
        start = input("Enter starting node: ")
        print("DFS Traversal:")
        dfs(graph, start, set())
    elif choice == '3':
        break
    else:
        print("Invalid choice")
