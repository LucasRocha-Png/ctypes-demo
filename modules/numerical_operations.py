"""
This script imports the "numerical_operations.so" file, compilled with the command 
"g++ -fPIC -shared -static -o numerical_operations.so numerical_operations.cpp" at numerical_operations folder,
and them, create a function that calls the C++ functions.
To create a .so file you must have MinGW.

This file declares the following functions:
add_two_int
add_two_float
add_two_double
"""

import ctypes
import os

archive_folder = os.path.dirname(__file__)

library = ctypes.CDLL(f"{archive_folder}\\numerical_operations\\numerical_operations.so")

#INT -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#From numerical_operations.so file, imports "add_two_int" function
add_two_int = library.add_two_int

#The input arguments types will be int and int (in ctypes its called c_int)
add_two_int.argtypes = [ctypes.c_int, ctypes.c_int]

#The output value type will be a int (in ctypes is called c_int)
add_two_int.restype = ctypes.c_int    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
    
    
#FLOAT -=-=-=-=-=-=-=-=-=-=
add_two_float = library.add_two_float
add_two_float.argtypes = [ctypes.c_float, ctypes.c_float]
add_two_float.restype = ctypes.c_float    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=  


#DOUBLE -=-=-=-=-=-=-=-=-=-=
add_two_double = library.add_two_double
add_two_double.argtypes = [ctypes.c_double, ctypes.c_double]
add_two_double.restype = ctypes.c_double   
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=     
    
if __name__ == "__main__":
    print("Adding two int - (20, 20)")
    print(add_two_int(20,20))
    
    print("Adding two float - (20, 20)")
    print(add_two_float(20,20))
    
    print("Adding two double - (20, 20)")
    print(add_two_double(20,20))
