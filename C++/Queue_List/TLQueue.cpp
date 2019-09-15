#include "TLQueue.h"

void TLQueue::enqueue(int value) {
  Node* insertee = new Node(value);
  if (empty()) {
    m_head = insertee;
    m_tail = m_head;
    return;
  }
  m_tail->set_next(insertee);
  m_tail = insertee;
  m_size++;
}
int TLQueue::dequeue() {
  if (empty()) {
    std::cout << "Queue is empty." << std::endl;
    return -1;
  }
  Node* out = m_head;
  m_head = out->next();
  int res = out->get();
  delete out;
  m_size--;
  return res;
}

bool TLQueue::empty() const { return m_head == nullptr; }