#include <iostream>
#include <climits>

using namespace std;

const int MAX = 100;
int graph[MAX][MAX];
bool visited[MAX];

int main() {
    int n, edges;
    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter number of edges: ";
    cin >> edges;

    // Initialize graph with 0s
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            graph[i][j] = 0;
    // Enter digits not charecters
    cout << "Enter edges (source destination weight):\n";
    for (int i = 0; i < edges; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        u--; v--; // Convert to 0-based indexing
        graph[u][v] = w;
        graph[v][u] = w; // undirected
    }

    // Initialize visited array
    for (int i = 0; i < n; i++)
        visited[i] = false;

    visited[0] = true; // Start from vertex 1 (index 0)
    int edgeCount = 0, totalCost = 0;

    cout << "\nEdges in MST:\n";

    while (edgeCount < n - 1) {
        int minEdge = INT_MAX;
        int u = -1, v = -1;

        // Pick the smallest edge from visited to unvisited
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                for (int j = 0; j < n; j++) {
                    if (!visited[j] && graph[i][j]) {
                        if (graph[i][j] < minEdge) {
                            minEdge = graph[i][j];
                            u = i;
                            v = j;
                        }
                    }
                }
            }
        }

        if (u != -1 && v != -1) {
            cout << (u + 1) << " - " << (v + 1) << " : " << graph[u][v] << endl;
            visited[v] = true;
            totalCost += graph[u][v];
            edgeCount++;
        } else {
            cout << "Graph is not connected. MST not possible.\n";
            return 0;
        }
    }

    cout << "Total cost of MST: " << totalCost << endl;
    return 0;
}
