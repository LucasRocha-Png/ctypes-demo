"""
This script imports the "number_operations.so" file, compilled with the command 
"g++ -shared -static -o number_operations.so number_operations.cpp" at number_operations folder,
and them, create a function that calls the C++ functions.

To create a .so file must have MinGW.

Declares:

add_two_int
add_two_float
add_two_double
"""

import ctypes
import os

archive_folder = os.path.dirname(__file__)

library = ctypes.CDLL(f"number_operations\\number_operations.so")

#INT -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#From number_operations.so file, imports "add_two_int" function
add_two_int_ = library.add_two_int

#The input arguments types will be int and int (in ctypes its called c_int)
add_two_int_.argtypes = [ctypes.c_int, ctypes.c_int]

#The output value type will be a int (in ctypes is called c_int)
add_two_int_.restype = ctypes.c_int    
    
#Create a function that calls the C++ function. Thats a good practice to not import every single time the .so file
def add_two_int(a, b):
    global add_two_int_
    return add_two_int_(a,b)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
    
    
#FLOAT -=-=-=-=-=-=-=-=-=-=
add_two_float_ = library.add_two_float
add_two_float_.argtypes = [ctypes.c_float, ctypes.c_float]
add_two_float_.restype = ctypes.c_float    
def add_two_float(a, b):
    global add_two_float_
    return add_two_float_(a,b)    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=  


#DOUBLE -=-=-=-=-=-=-=-=-=-=
add_two_double_ = library.add_two_double
add_two_double_.argtypes = [ctypes.c_double, ctypes.c_double]
add_two_double_.restype = ctypes.c_double   
def add_two_double(a, b):
    global add_two_double_
    return add_two_double_(a,b)    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=     
    
if __name__ == "__main__":
    print("Adding two int - (20, 20)")
    print(add_two_int(20,20))
    
    print("Adding two float - (20, 20)")
    print(add_two_float(20,20))
    
    print("Adding two double - (20, 20)")
    print(add_two_double(20,20))
