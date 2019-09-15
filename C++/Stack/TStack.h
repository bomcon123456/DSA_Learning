#ifndef TSTACK
#define TSTACK

class TStack {
  static const int GROWTH_FACTOR = 2;
  static const int SHRINK_FACTOR = 4;

 public:
  TStack();

  void push(int value);
  int pop();
  bool is_empty() const { return m_size == 0; };

  void debug();

 private:
  int* m_data;
  int m_size;
  int m_capacity;

  void resize(int capacity);
};

#endif