#ifndef TVECTOR
#define TVECTOR

class TVector {
  static const int MIN_CAPACITY = 16;
  static const int GROWTH_FACTOR = 2;
  static const int SHRINK_FACTOR = 4;

 public:
  TVector(int capacity);
  TVector(TVector& other) = default;

  int size();
  int capacity();
  bool is_empty();
  int at(int idx);
  void push(const int& item);
  void insert(int idx, const int& item);
  void prepend(const int& item);
  int pop();
  int delete_index(int idx);
  void remove(const int& item);
  int find(const int& item);

  void debug() const;

 private:
  int* m_data;
  int m_size;
  int m_capacity;

  void resize(int capacity);
  int calculate_capacity(int capacity) const;
};

#endif  //  TVECTOR