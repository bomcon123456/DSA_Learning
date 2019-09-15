#include "TList.h"

int main() {
  TList test;
  for (int i = 16; i > 0; --i) {
    test.push_front(i);
  }
  test.pop_front();
  test.pop_back();
  test.insert(5, 7);
  // test.erase(5);
  test.remove_value(15);
  test.reverse();
  test.debug();
  std::cout << std::endl << "-----" << std::endl;
  // std::cout << test.front() << " " << test.back() << std::endl;
  // std::cout << test.value_at(11) << std::endl;
  std::cout << test.value_n_from_end(4) << std::endl;
}