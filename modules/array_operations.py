"""
This script imports the "array_operations.so" file, compilled with the command 
"g++ -fPIC -shared -static -o array_operations.so array_operations.cpp" at array_operations folder,
and them, create a function that calls the C++ functions.
To create a .so file you must have MinGW.


Explanation:
Working with "arrays" in ctypes is a little weird for python users.
Instead of sending a python array like we are used to, we send the array pointer. We do it allocating memory using ctypes, and sending
the pointer as our array


This file declares the following functions:
reverse_string
"""

import ctypes
import os

archive_folder = os.path.dirname(__file__)

library = ctypes.CDLL(f"{archive_folder}\\array_operations\\array_operations.so")

#SUM LIST -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Instead of doing like we used to do in the others bases, probably the best way of working with arrays ->
#is doing a python function instead of importing the c function directally. But first:

#From array_operations.so file, imports "sum_list" function
sum_list_ = library.sum_list

#The input arguments types will be a pointer that points to a int list and a int (in ctypes its called ctypes.POINTER(ctypes.c_int) and c_int)
sum_list_.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)

#The output value type will be a int (in ctypes is called c_int)
sum_list_.restype = ctypes.c_int


def sum_list(array):
    global sum_list_
    
    #First, we create a variable, that assigns an space at the memory for our values
    #This will open at the memory a quantity of blocks of the size of our array, that accepts only the int type, and automaticaly assigning the values of our array on it
    values = (ctypes.c_int * len(array))(*array) 

    #Now we call and return the c function, but instead of passing the python array, we pass the pointer variable we created
    return sum_list_(values, len(array))
    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

if __name__ == "__main__":
    print(sum_list([33, 20]))
   
