# ctypes-demo
This repository is useful to understand how to import, and how C++ libraries works in Python.
It can also be useful to use as a base for your program.

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



# Bases to use
These bases are useful to understand how to work with ctypes and with all kind off types of C language.
## number_operations.py
### add_two_int
Sums two int numbers

### sum_two_floats
Sum two float numbers

### sum_two_double
Sum two double numbers

## string_operations.py
### reverse_string
Return a reversed string
