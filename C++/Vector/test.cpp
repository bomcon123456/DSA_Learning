#include <iostream>
#include "tvector.h"

int main() {
  TVector test(16);
  for (int i = 0; i < 17; i++) test.push(i);
  test.delete_index(5);
  test.delete_index(5);
  test.delete_index(5);
  test.delete_index(5);
  test.delete_index(5);
  test.delete_index(5);
  test.delete_index(5);
  test.delete_index(5);
  test.prepend(1000);
  test.pop();
  test.pop();
  test.pop();
  test.pop();
  test.pop();
  test.pop();
  test.debug();

  return 0;
}