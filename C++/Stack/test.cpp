#include <iostream>
#include "TStack.h"

int main() {
  TStack test;
  for (int i = 1; i < 20; ++i) {
    test.push(i);
  }
  test.pop();
  test.debug();
}