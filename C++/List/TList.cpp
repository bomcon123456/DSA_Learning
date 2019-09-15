#include "TList.h"

int TList::value_at(int idx) {
  if (idx > m_size || idx < 1) {
    std::cout << "Invalid index" << std::endl;
    exit(EXIT_FAILURE);
  }
  Node* cur = m_root;
  while (idx > 0) {
    cur = cur->next();
    idx--;
  }
  return cur->get();
}
void TList::push_front(int value) {
  Node* node = new Node(value, m_root);
  m_root = node;
  m_size++;
}

int TList::pop_front() {
  if (m_root == nullptr) {
    std::cout << "List is empty." << std::endl;
    return -1;
  }
  Node* temp = m_root;
  int res = temp->get();
  m_root = temp->next();
  delete temp;
  m_size--;
  return res;
}

void TList::pop_back() {
  Node* cur = m_root;
  Node* prev = m_root;
  while (cur->next() != nullptr) {
    prev = cur;
    cur = cur->next();
  }
  prev->set_next(nullptr);
  delete cur;
  m_size--;
  // delete cur;
}

int TList::front() { return m_root->get(); }
int TList::back() {
  Node* cur = m_root;

  while (cur->next() != nullptr) {
    cur = cur->next();
  }
  return cur->get();
}
void TList::insert(int idx, int value) {
  if (idx > m_size || idx < 1) {
    std::cout << "Invalid index" << std::endl;
    exit(EXIT_FAILURE);
  }
  Node* cur = m_root;
  idx--;
  Node* insertee = new Node(value);
  while (idx > 1) {
    cur = cur->next();
    idx--;
  }
  insertee->set_next(cur->next());
  cur->set_next(insertee);
  m_size++;
}
int TList::erase(int idx) {
  if (idx > m_size || idx < 1) {
    std::cout << "Invalid index" << std::endl;
    exit(EXIT_FAILURE);
  }
  if (idx == 1) {
    return pop_front();
  }
  idx--;
  Node* cur = m_root;
  while (idx > 1) {
    cur = cur->next();
    idx--;
  }
  Node* pre_deletee = cur;
  Node* deletee = cur->next();
  pre_deletee->set_next(deletee->next());
  // std::cout << "Pre delete:" << cur->get() << std::endl;
  // cur->set_next(deletee->next());
  int res = deletee->get();
  delete deletee;
  m_size--;
  return res;
}
int TList::value_n_from_end(int n) {
  int index = m_size - n - 1;
  Node* cur = m_root;

  while (index > 1) {
    cur = cur->next();
    index--;
  }
  return cur->next()->get();
}
void TList::reverse() {
  Node* cur = m_root;
  Node* prev = nullptr;
  Node* next = m_root->next();

  while (next != nullptr) {
    cur->set_next(prev);
    prev = cur;
    cur = next;
    next = next->next();
  }
  cur->set_next(prev);
  m_root = cur;
}
void TList::remove_value(int value) {
  Node* cur = m_root;
  int i = 1;
  while (cur->next() != nullptr) {
    if (cur->get() == value) {
      std::cout << i << std::endl;
      erase(i);
      return;
    }
    cur = cur->next();
    i++;
  }
  if (cur->get() == value) {
    std::cout << i << std::endl;
    erase(i);
    return;
  }
}

void TList::debug() const {
  std::cout << "size: " << m_size << std::endl << "items: " << std::endl;
  Node* cur = m_root;
  int i = 1;
  while (cur->next() != nullptr) {
    printf("%d: %d", i++, cur->get());
    std::cout << std::endl;
    cur = cur->next();
  }
  printf("%d: %d", i, cur->get());
}