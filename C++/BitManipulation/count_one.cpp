// Count number of ones in a number's base 2 representation
#include <iostream>

int count_one(int x)
{
  int count = 0;
  while (x)
  {
    x = x & (x - 1);
    count++;
  }
  return count;
}

int main()
{
  int a = 3;
  std::cout << count_one(a) << std::endl;
}