"""
This script imports the "cmake_operations.dll" file, compilled with the command 
"cmake .." "cmake --build ." at cmake_operations/build/ folder,
and them, create a function that calls the C++ functions.
To create a .DLL or .SO (depending of your operating system) file you must have CMake.

This file declares the following functions:
hello
"""


import ctypes
import os


archive_folder = os.path.dirname(__file__)

library = ctypes.CDLL(f"cmake_operations/build/libcmake-tests.so")

#Print Hello
library.hello()

