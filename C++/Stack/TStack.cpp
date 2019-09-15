#include "TStack.h"
#include <iostream>

TStack::TStack() {
  m_size = 0;
  m_capacity = 1;
  m_data = new int[m_capacity];
}
void TStack::resize(int capacity) {
  if (capacity < 1) {
    std::cout << "Can't resize array." << std::endl;
  }
  int* temp = m_data;
  m_data = new int[capacity];
  for (int i = 0; i < m_size; i++) {
    m_data[i] = temp[i];
  }
  delete[] temp;
  m_capacity = capacity;
}

void TStack::push(int value) {
  if (m_size == m_capacity) {
    resize(m_capacity * GROWTH_FACTOR);
  }
  m_data[m_size++] = value;
}
int TStack::pop() {
  if (is_empty()) {
    std::cout << "Stack's empty" << std::endl;
    return -1;
  }
  int res = m_data[--m_size];
  if (m_size <= m_capacity / SHRINK_FACTOR) {
    resize(m_capacity / GROWTH_FACTOR);
  }
  return res;
}

void TStack::debug() {
  std::cout << "Size: " << m_size << std::endl;
  std::cout << "Capacity: " << m_capacity << std::endl;
  for (int i = 0; i < m_size; ++i) {
    std::cout << i << ": " << m_data[i] << std::endl;
  }
}