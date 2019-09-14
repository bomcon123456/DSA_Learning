#include <iostream>

void subsets(char A[], int N)
{
  for (int i = 0; i < (1 << N); ++i)
  {
    for (int j = 0; j < N; ++j)
    {
      if (i & (1 << j))
        std::cout << A[j] << ' ';
    }
    std::cout << std::endl;
  }
}

int main()
{
  char a[5] = {'a', 'b', 'c', 'd', 'e'};
  subsets(a, 5);
  return 0;
}