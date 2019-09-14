#include <iostream>

class A
{
  private:
    int a;
  public:
    void run(){
      std::cout<<"LOL"
    }
}

class B
{
  private:
    int b;
  public:
    void run(){
      std::cout<<"lol"
    }
}

class C: A,B {
  private:
    int c;
}

int main()
{
  C test;
  test.run()
}