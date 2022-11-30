"""
This script imports the "string_operations.so" file, compilled with the command 
"g++ -fPIC -shared -static -o string_operations.so string_operations.cpp" at string_operations folder,
and them, create a function that calls the C++ functions.
To create a .so file you must have MinGW.


Explanation:
Working with "strings" in ctypes is a little weird for python users.
Instead of sending a python string like we are used to, we send a string in bytes. We do it just putting a letter b at the beggining,
like we do in a f-string.
Later, you need to decode back the returned value, you do it >creating a variable< of the returned value
and them using "str(variable_name, UTF-8)" or "variable_name.decoded()"
For some reason, you cannot decode directally in the function like "str(function('string'), UTF-8)", you must create a variable.


This file declares the following functions:
reverse_string
"""

import ctypes
import os

archive_folder = os.path.dirname(__file__)

library = ctypes.CDLL(f"{archive_folder}\\string_operations\\string_operations.so")


#REVERSE STRING -=-=-=-=-=-=-=-=-=-
#From string_operations.so file, imports "reverse_string" function
reverse_string = library.reverse_string

#The input argument type will be a char pointer (in ctypes its called c_char_p)
reverse_string.argtype = ctypes.c_char_p

#The output value type will be a char (in ctypes is called c_char_p)
reverse_string.restype = ctypes.c_char_p    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

if __name__ == "__main__":

    #Read the explanation at the header of the file.

    string = reverse_string(b'Hello World')
    
    print("String without decoding:")
    print(string)
    print()
    print("String decoded:")
    print(str(string, "UTF-8"))
