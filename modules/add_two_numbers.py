"""
This script imports the "add_two_numbers.so" made with "g++ -shared -static -o add_two_numbers.so add_two_numbers.cpp"
and them, create a function that calls the C++ function
"""

import ctypes

#From add_two_numbers, imports "add_two_numbers" function
function = ctypes.CDLL("./add_two_numbers.so").add_two_numbers

#The input arguments types will be int and int (in ctypes its called c_int)
function.argtypes = [ctypes.c_int, ctypes.c_int]
    
#Create a function that calls the C++ function. Thats a good practice to not import every single time the .so file
def add_two_numbers(a, b):
    global function
    
    return function(a,b)

