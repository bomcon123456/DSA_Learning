#include "tvector.h"
#include <iostream>

TVector::TVector(int capacity) {
  if (capacity < 1) {
    std::cout << "Can't initiate vector with this size." << std::endl;
    exit(EXIT_FAILURE);
  }
  m_capacity = calculate_capacity(capacity);
  m_size = 0;
  m_data = new int[m_capacity];
  std::cout << m_capacity << std::endl;
}

int TVector::calculate_capacity(int capacity) const {
  int result = MIN_CAPACITY;
  while (result < capacity) {
    result *= GROWTH_FACTOR;
  }
  return result;
}

void TVector::resize(int capacity) {
  int* temp = m_data;
  m_data = new int[capacity];
  m_capacity = capacity;
  for (int i = 0; i < m_size; ++i) {
    m_data[i] = temp[i];
  }
  delete[] temp;
}

int TVector::size() { return m_size; }
int TVector::capacity() { return m_capacity; }
bool TVector::is_empty() { return m_size == 0; }
int TVector::at(int idx) { return *(m_data + sizeof(int) * idx); }
void TVector::push(const int& item) {
  if (m_size == m_capacity) {
    resize(m_capacity * GROWTH_FACTOR);
  }
  m_data[m_size++] = item;
}

void TVector::insert(int idx, const int& item) {
  if (m_size == m_capacity) {
    resize(m_capacity * GROWTH_FACTOR);
  }
  for (int i = m_size - 1; i >= idx; --i) {
    m_data[i + 1] = m_data[i];
  }
  m_data[idx] = item;
  m_size++;
}
void TVector::prepend(const int& item) { return insert(0, item); }
int TVector::pop() {
  if (m_size == 0) {
    std::cout << "Vector's empty." << std::endl;
    return -1;
  }
  int res = m_data[--m_size];
  if (m_size <= m_capacity / SHRINK_FACTOR) {
    resize(m_capacity / GROWTH_FACTOR);
  }
  return res;
}
int TVector::delete_index(int idx) {
  if (idx < 0 || idx > m_size) {
    std::cout << "Invalid index" << std::endl;
  }
  idx--;
  int res = m_data[idx];
  for (int i = idx; i < m_size - 1; i++) {
    m_data[i] = m_data[i + 1];
  }
  --m_size;
  if (m_size <= m_capacity / SHRINK_FACTOR) {
    resize(m_capacity / GROWTH_FACTOR);
  }
  return res;
}
void TVector::remove(const int& item) {
  for (int i = 0; i < m_size; ++i) {
    if (m_data[i] == item) {
      delete_index(i);
      i--;
    }
  }
}
int TVector::find(const int& item) {
  for (int i = 0; i < m_size; i++) {
    if (m_data[i] == item) return i;
  }
  return -1;
}

void TVector::debug() const {
  std::cout << "size: " << m_size << std::endl
            << "capacity: " << m_capacity << std::endl
            << "items: " << std::endl;

  for (int i = 0; i < m_size; ++i) {
    printf("%d: %d", i, m_data[i]);
    std::cout << std::endl;
  }
}