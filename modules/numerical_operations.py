"""
This script imports the "numerical_operations.so" file, compilled with the command 
"g++ -fPIC -shared -static -o numerical_operations.so numerical_operations.cpp" at numerical_operations folder,
and them, create a function that calls the C++ functions.
To create a .so file you must have MinGW.

This file declares the following functions:
sum_two_int
sum_two_float
sum_two_double
"""

import ctypes
import os

archive_folder = os.path.dirname(__file__)

library = ctypes.CDLL(f"{archive_folder}\\numerical_operations\\numerical_operations.so")

#INT -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#From numerical_operations.so file, imports "sum_two_int" function
sum_two_ints = library.sum_two_ints

#The input arguments types will be int and int (in ctypes its called c_int)
sum_two_ints.argtypes = [ctypes.c_int, ctypes.c_int]

#The output value type will be a int (in ctypes is called c_int)
sum_two_ints.restype = ctypes.c_int    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
    
    
#FLOAT -=-=-=-=-=-=-=-=-=-=
sum_two_floats = library.sum_two_floats
sum_two_floats.argtypes = [ctypes.c_float, ctypes.c_float]
sum_two_floats.restype = ctypes.c_float    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=  


#DOUBLE -=-=-=-=-=-=-=-=-=-=
sum_two_doubles = library.sum_two_doubles
sum_two_doubles.argtypes = [ctypes.c_double, ctypes.c_double]
sum_two_doubles.restype = ctypes.c_double   
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=     
    
if __name__ == "__main__":
    print("suming two ints - (20, 20)")
    print(sum_two_ints(20,20))
    
    print("suming two floats - (20, 20)")
    print(sum_two_floats(20,20))
    
    print("suming two doubles - (20, 20)")
    print(sum_two_doubles(20,20))
