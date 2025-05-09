def is_safe(node, color, graph, colors, n):
    for k in range(n):
        if graph[node][k] == 1 and colors[k] == color:
            return False
    return True

def graph_coloring(graph, m, colors, node, n):
    if node == n:
        return True
    
    for clr in range(1, m+1):
        if is_safe(node, clr, graph, colors, n):
            colors[node] = clr
            if graph_coloring(graph, m, colors, node+1, n):
                return True
            colors[node] = 0  # Backtrack
    return False

def solve_coloring_problem(graph, m):
    n = len(graph)
    colors = [0] * n
    if graph_coloring(graph, m, colors, 0, n):
        print("Solution exists: ", colors)
    else:
        print("No solution exists.")

# Example graph: 4 vertices in a square (cycle)
graph = [
    [0, 1, 0, 1],  # Vertex 0 is connected to 1 and 3
    [1, 0, 1, 0],  # Vertex 1 is connected to 0 and 2
    [0, 1, 0, 1],  # Vertex 2 is connected to 1 and 3
    [1, 0, 1, 0]   # Vertex 3 is connected to 0 and 2
]

# Number of colors
m = 3

solve_coloring_problem(graph, m)
