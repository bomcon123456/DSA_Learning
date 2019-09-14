#include <iostream>
#include <vector>

using namespace std;

bool is_attacked(int x, int y, vector< vector<bool> >& board, int n)
{
  int offset_x[2] = {1, -1};
  int offset_y[2] = {1, -1};
  for (int i = 0; i < n; ++i)
  {
    if (board[x][i])
    {
      return true;
    }
    if (board[i][y])
    {
      return true;
    }
  }
  for (int i = 0; i < 2; ++i)
  {
    for (int j = 0; j < 2; ++j)
    {
      int nx = x, ny = y;
      while ((nx > -1 && nx < n) && (ny > -1 && ny < n))
      {
        if (board[nx][ny])
          return true;
        nx += offset_x[i];
        ny += offset_y[j];
      }
    }
  }
  return false;
}

bool nqueens(vector< vector<bool> >& board, int n, int col)
{
  if (col >= n)
    return true;
  for (int i = 0; i < n; ++i)
  {
      if (is_attacked(i, col, board, n))
      {
        continue;
      }
      board[i][col] = true;
      if (nqueens(board, n, col + 1))
        return true;
      board[i][col] = false;
  }
  return false;
}

int main()
{
  int queens;
  cin >> queens;
  // queens = 4;
  vector< vector<bool> > board(queens, vector<bool>(queens, false));
  bool flag = nqueens(board, queens, 0);
  if (flag)
  {
    cout << "YES" << endl;
    for(int i=0; i<queens; ++i){
      for(int j =0 ;j < queens; ++j){
        cout<< board[i][j] << " ";
      }
      cout <<endl;
    }
  }
  else
  {
    cout << "NO";
  }
  return 0;
}