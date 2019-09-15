#include <iostream>
#include "queuea.h"

int main() {
  TAQueue test;
  for (int i = 1; i < 9; ++i) {
    test.enqueue(i);
  }
  test.dequeue();
  test.dequeue();
  test.dequeue();
  test.enqueue(100);
  test.dequeue();
  test.dequeue();
  test.dequeue();
  test.dequeue();
  test.dequeue();
  test.dequeue();
  for (int i = 1; i < 9; ++i) {
    test.enqueue(i);
  }
  test.dequeue();

  test.debug();
}