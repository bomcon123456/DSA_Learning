#include "TLQueue.h"

int main() {
  TLQueue test;
  std::cout << test.empty() << std::endl;
  test.enqueue(1);
  std::cout << test.empty() << std::endl;
  std::cout << "DEQUEUEd: " << test.dequeue() << std::endl;
  std::cout << test.empty() << std::endl;
}