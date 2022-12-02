#include <iostream>
#include <typeinfo>

extern "C"{
	#include "array_operations.h"
	int sum_list(int *list, int size_list){
		int sum = 0;
		for (int i = 0; i < size_list; i++){
			int value = list[i];
			sum += value;
		}
		return sum;
	}

	char** reversed_list(char** list, int size_list){

		for (int i = 0, j = size_list - 1; i < size_list/2; i++, j--)  
		{     
			char* temp = list[i];  
			list[i] = list[j];  
			list[j] = temp;  
		}  

		return list;
	}
	
}