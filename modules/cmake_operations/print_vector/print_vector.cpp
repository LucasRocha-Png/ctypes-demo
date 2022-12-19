#include <iostream>
#include <vector>
#include "print_vector.hpp"

void print_vector(std::vector<int> list){
	for (int value : list){
		std::cout << value << "\n";
	}
}