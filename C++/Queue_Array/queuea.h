#ifndef QUEUEARRAY
#define QUEUEARRAY

class TAQueue {
 public:
  TAQueue();

  void enqueue(int value);
  int dequeue();
  bool empty() const;
  void debug() const;

 private:
  int* m_data;
  int m_capacity;
  int m_size;
  int m_start;
  int m_end;
};

#endif  // !QUEUEARRAY