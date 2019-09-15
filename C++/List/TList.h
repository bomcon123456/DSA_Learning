#ifndef TLIST
#define TLIST

#include <iostream>

class Node {
 public:
  Node(int value) : m_item(value), m_next(nullptr) {}
  Node(int value, Node* ptr) : m_item(value), m_next(ptr) {}

  friend std::ostream& operator<<(std::ostream& out, const Node& n) {
    out << n.m_item;
    return out;
  }

  Node* next() { return m_next; }
  void set_next(Node* n) { m_next = n; }
  void set(int n) { m_item = n; }
  int get() { return m_item; }

 private:
  int m_item;
  Node* m_next;
};

class TList {
 public:
  TList() : m_root(nullptr), m_size(0) {}

  int size() const { return m_size; }
  int empty() const { return m_size == 0; }

  void debug() const;

  int value_at(int idx);
  void push_front(int value);
  int pop_front();
  void pop_back();
  int front();
  int back();
  void insert(int idx, int value);
  int erase(int idx);
  int value_n_from_end(int n);
  void reverse();
  void remove_value(int value);

 private:
  Node* m_root;
  int m_size;
};

#endif
