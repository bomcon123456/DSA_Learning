#ifndef TLQUEUE_H
#define TLQUEUE_H

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

class TLQueue {
 public:
  TLQueue() : m_head(nullptr), m_tail(nullptr), m_size(0) {}

  void enqueue(int value);
  int dequeue();
  bool empty() const;

 private:
  Node* m_head;
  Node* m_tail;
  int m_size;
};

#endif