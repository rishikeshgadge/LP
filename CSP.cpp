#include <iostream>
using namespace std;

bool isSafe(int row, int col, int **board, int n) {
  // Check left side of the current row
  for (int i = 0; i < col; i++) {
    if (board[row][i] == 1) return false;
  }

  // Check upper diagonal (left side)
  for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
    if (board[i][j] == 1) return false;
  }

  // Check lower diagonal (left side)
  for (int i = row, j = col; i < n && j >= 0; i++, j--) {
    if (board[i][j] == 1) return false;
  }

  return true;
}

bool solveNQueens(int **board, int col, int n) {
  if (col >= n) {
    return true;
  }

  for (int i = 0; i < n; i++) {
    if (isSafe(i, col, board, n)) {
      board[i][col] = 1;

      if (solveNQueens(board, col + 1, n)) {
        return true;
      }

      board[i][col] = 0; // Backtrack
    }
  }
  return false;
}

void printSolution(int **board, int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << board[i][j] << " ";
    }
    cout << endl;
  }
}

int main() {
  int n;
  cout << "Enter the board size (n): ";
  cin >> n;
  
  int** board = new int*[n];
  for (int i = 0; i < n; i++) {
      board[i] = new int[n](); // Initialize all elements to 0
  }
  
  if (solveNQueens(board, 0, n)) {
    cout << "Solution exists:" << endl;
    printSolution(board, n);
  } else {
    cout << "No solution exists" << endl;
  }

  // Free allocated memory
  for (int i = 0; i < n; i++) {
      delete[] board[i];
  }
  delete[] board;

  return 0;
}
