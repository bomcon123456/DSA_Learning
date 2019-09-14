#include <iostream>

int count_bit_set(int x)
{
  int count = 0;
  while (x)
  {
    if (x & 1)
      count++;
    x = x >> 1;
  }
  return count;
}

int main()
{
  std::cout << count_bit_set(8) << std::endl;
  return 0;
}