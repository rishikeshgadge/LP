#include <iostream>
#include <climits>

using namespace std;

const int MAX = 100;
int graph[MAX][MAX];
bool visited[MAX];
int dist[MAX];

int findMinDist(int n) {
    int min = INT_MAX, index = -1;
    for (int i = 0; i < n; i++) {
        if (!visited[i] && dist[i] < min) {
            min = dist[i];
            index = i;
        }
    }
    return index;
}

int main() {
    int n, edges;
    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter number of edges: ";
    cin >> edges;

    // Initialize graph with 0
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            graph[i][j] = 0;
            

    cout << "Enter edges (source destination weight):\n";
    for (int i = 0; i < edges; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        u--; v--; // Convert to 0-based indexing
        graph[u][v] = w;
        graph[v][u] = w; // Undirected graph 
    }

    int start;
    cout << "Enter source vertex (1 to " << n << "): ";
    cin >> start;
    start--; // 0-based

    // Initialize distances and visited
    for (int i = 0; i < n; i++) {
        dist[i] = INT_MAX;
        visited[i] = false;
    }
    dist[start] = 0;

    for (int count = 0; count < n - 1; count++) {
        int u = findMinDist(n);
        if (u == -1) break;
        visited[u] = true;

        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    cout << "\nShortest distances from vertex " << (start + 1) << ":\n";
    for (int i = 0; i < n; i++) {
        cout << "To vertex " << (i + 1) << " : ";
        if (dist[i] == INT_MAX)
            cout << "Unreachable\n";
        else
            cout << dist[i] << endl;
    }

    return 0;
}
