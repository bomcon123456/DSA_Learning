#include <iostream>

long largest_power_of_two(long N)
{
  N = N | (N >> 1);
  N = N | (N >> 2);
  N = N | (N >> 4);
  N = N | (N >> 8);

  // now N = 2*x + 1
  return (N + 1) >> 1;
}

int main()
{
  std::cout << largest_power_of_two(20) << std::endl;
}