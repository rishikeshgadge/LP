#include <iostream>
using namespace std;

struct Edge {
    int src, dest, weight;
};

// Function to find the parent of a vertex (with path compression)
int find(int parent[], int vertex) {
    while (vertex != parent[vertex]) {
        parent[vertex] = parent[parent[vertex]];  // Path compression
        vertex = parent[vertex];
    }
    return vertex;
}

// Function to union two sets
void unionSets(int parent[], int x, int y) {
    int rootX = find(parent, x);
    int rootY = find(parent, y);
    parent[rootY] = rootX;
}

// Bubble sort edges by weight
void sortEdges(Edge edges[], int edgeCount) {
    for (int i = 0; i < edgeCount - 1; i++) {
        for (int j = 0; j < edgeCount - i - 1; j++) {
            if (edges[j].weight > edges[j + 1].weight) {
                Edge temp = edges[j];
                edges[j] = edges[j + 1];
                edges[j + 1] = temp;
            }
        }
    }
}

// Kruskal's algorithm
void kruskalMST(int vertices, Edge edges[], int edgeCount) {
    Edge mst[100]; // assuming max 100 edges
    int mstIndex = 0;
    int totalWeight = 0;
    int parent[100]; // assuming max 100 vertices

    // Initialize parent array
    for (int i = 0; i < vertices; i++) {
        parent[i] = i;
    }

    // Sort edges by weight
    sortEdges(edges, edgeCount);

    // Process each edge
    for (int i = 0; i < edgeCount; i++) {
        int src = edges[i].src;
        int dest = edges[i].dest;
        int srcRoot = find(parent, src);
        int destRoot = find(parent, dest);

        if (srcRoot != destRoot) {
            mst[mstIndex++] = edges[i];
            totalWeight += edges[i].weight;
            unionSets(parent, srcRoot, destRoot);
        }

        if (mstIndex == vertices - 1) {
            break;
        }
    }

    // Output the MST
    cout << "Edges in the Minimum Spanning Tree:\n";
    for (int i = 0; i < mstIndex; i++) {
        cout << "Edge: " << mst[i].src << " - " << mst[i].dest<< ", Weight: " << mst[i].weight << std::endl;
    }
    cout << "Total MST Weight: " << totalWeight << std::endl;
}

int main() {
    int vertices = 4;
    int edgeCount = 5;

    Edge edges[5] = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    kruskalMST(vertices, edges, edgeCount);

    return 0;
}
