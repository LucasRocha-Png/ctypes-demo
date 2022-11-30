
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
}