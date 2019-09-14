#include <iostream>

bool isPowerOfTwo(int x)
{
  // (1) x != 0
  // (x-1) -> the rightmost 1 and bits right to it are flipped
  // (2) if x = 2^k -> x = (100...000) base 2
  // x-1 = (0111.111) base 2
  // x & (x-1) = (0) base 2
  // -> !(those) = 1
  return (x && !(x & (x - 1)));
}

int main()
{
  int a = 4;
  std::cout << isPowerOfTwo(a) << std::endl;

  return 0;
}