#include <cstring>

extern "C"{
	#include "string_operations.h"
	char* reverse_string(char* str){
		return strrev(str);
	}
}
