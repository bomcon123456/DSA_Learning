#include "queuea.h"

#include <iostream>

TAQueue::TAQueue() {
  m_size = 0;
  m_capacity = 8;
  m_data = new int[m_capacity];
  m_start = 0;
  m_end = 0;
}

void TAQueue::enqueue(int value) {
  if (m_size == m_capacity) {
    std::cout << "Queue is full." << std::endl;
    exit(EXIT_FAILURE);
  }
  m_data[m_start] = value;
  m_size++;
  m_start = (m_start + 1) % m_capacity;
}
int TAQueue::dequeue() {
  if (empty()) {
    std::cout << "Queue is empty." << std::endl;
    return -1;
  }
  int res = m_data[m_end];
  m_data[m_end] = 0;
  m_end = (m_end + 1) % m_capacity;
  m_size--;
}

bool TAQueue::empty() const { return m_size == 0; }

void TAQueue::debug() const {
  std::cout << "Size: " << m_size << std::endl;
  for (int i = 0; i < m_capacity; i++) {
    std::cout << "i: " << m_data[i] << std::endl;
  }
  // int cur = m_end;
  // int i = 0;
  // if (m_size == m_capacity) {
  //   while (cur != (m_start - 1 + m_capacity) % m_capacity) {
  //     std::cout << i << ": " << m_data[i] << std::endl;
  //     cur = (cur + 1) % m_capacity;
  //     i++;
  //   }
  //   std::cout << i << ": " << m_data[i] << std::endl;
  //   return;
  // }
  // while (cur != m_start) {
  //   std::cout << i << ": " << m_data[i] << std::endl;
  //   cur = (cur + 1) % m_capacity;
  //   i++;
  // }
}
