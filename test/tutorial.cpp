#include <iostream>

inline void print_result(int a, int b){ std::cout << a + b << "\n";}

//All functions that will be EXPORTED must be in ' extern "C" ' scope
//If you have an additional function like the exemple above, you don't need so.
extern "C"
{
  int add_two_numbers(int a, int b){
    print_result(a, b);
    return a + b;
  }
}