#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

const int MAX = 100;
vector<pair<int, int>> graph[MAX]; // adjacency list: (neighbor, weight)
bool visited[MAX];

int main() {
    int n, edges;
    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter edges (source destination weight):\n";
    for (int i = 0; i < edges; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        u--; v--; // Convert to 0-based indexing
        graph[u].push_back({v, w});
        graph[v].push_back({u, w}); // Undirected
    }

    // Min-heap priority queue: (weight, vertex)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    int totalCost = 0;
    pq.push({0, 0}); // Start from vertex 0
    vector<bool> inMST(n, false);

    cout << "\nEdges in MST:\n";

    while (!pq.empty()) {
        auto [weight, u] = pq.top(); pq.pop();

        if (inMST[u]) continue;

        inMST[u] = true;
        totalCost += weight;

        if (weight != 0) // Skip printing the first dummy edge (0 cost)
            cout << "Included vertex " << (u + 1) << " with edge weight " << weight << endl;

        for (auto [v, w] : graph[u]) {
            if (!inMST[v]) {
                pq.push({w, v});
            }
        }
    }

    cout << "Total cost of MST: " << totalCost << endl;
    return 0;
}
