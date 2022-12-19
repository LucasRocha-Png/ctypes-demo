# ctypes-demo
This repository is useful to understand how to work, and how to import C/C++ libraries in Python. 
It also can be useful to use as a base for your program.

## Creating an C++ function
``` c++
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
```

## How to create an C++ external file for Python
``` bash
g++ -shared -static -o <destiny_file>.so <c_file>.cpp
```
P.S.: Make sure you have MinGW installed. If you get an error, check if you have the 64bits version installed.
#### Why to compile using -shared and -static at the same time???
If we used only -shared, the library wouldn't be able to call the "include" functions we set  


## Importing an external file in Python 
``` python
#Imports ctypes and os, you don't need to download nothing, it already comes with python
import ctypes
import os

#Take the path of the file to avoid problems
archive_folder = os.path.dirname(__file__)

#Imports the external file and assigns it to a variable
file_name = ""
library = ctypes.CDLL(f"{archive_folder}\\{file_name}.so") #Put de directory of the external file

#Import the function from the external file
add_two_numbers = library.add_two_numbers #library.{function you made}

#Set the data type of your function
#Check all data types in https://docs.python.org/3/library/ctypes.html
add_two_numbers.argtypes = [ctypes.c_int, ctypes.c_int] #Input values
add_two_numbers.restype = ctypes.c_int #Output value

#Now uses
add_two_numbers(20,30)
```



# Bases
These bases are useful to understand how to work with ctypes and with all kind off types of C language.

Each file contains functions that explain in detail how to work with the current type.
For exemple, number_operations.py contains "sum_two_int, sum_two_floats, sum_two_double" functions, that explain in detailed how to work with numerical types. In array_operations.py contains "sum_list" function, that explains in detailed how to work with arrays...

## number_operations.py
Explains how to work with numerical types.
### sum_two_ints
### sum_two_floats
### sum_two_doubles

## string_operations.py
Explains how to work with an string.
### reverse_string

## array_operations.py
Explains how to work with a array.
### sum_list

