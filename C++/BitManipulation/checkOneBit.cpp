#include <iostream>

bool check(int x, int i)
{
  if (x & (1 << i))
  {
    return true;
  }
  return false;
}

int main()
{
  int a = 8;
  std::cout << check(a, 3) << std::endl;
}