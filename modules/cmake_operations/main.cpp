/*

To build the main file uses "cmake ." and "cmake --build ." in build folder

*/


#include <iostream>
#include "main.hpp"

extern "C"{

	__declspec(dllexport) void  __cdecl hello(){
		std::cout << "Hello World" << "\n";
	}
}
