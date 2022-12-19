/*

To build the main file uses "cmake ." and "cmake --build ." in build folder

*/


#include <iostream>
#include <vector>
#include "main.hpp"
#include "print_vector/print_vector.cpp"

extern "C"{

	__declspec(dllexport) void  __cdecl hello(){
		std::cout << "Hello World" << "\n";
		
		std::vector<int> list = {1,2,3,4,5};
		print_vector(list);
	}
}
