#Imports ctypes and os, you don't need to download nothing, it already comes with python
import ctypes
import os

#Take the path of the file to avoid problems
archive_folder = os.path.dirname(__file__)

#Imports the external file and assigns it to a variable
file_name = "tutorial"
library = ctypes.CDLL(f"{archive_folder}\\{file_name}.so") #Put de directory of the external file

#Import the function from the external file
add_two_numbers = library.add_two_numbers #library.{function you made}

#Set the data type of your function
#Check all data types in https://docs.python.org/3/library/ctypes.html
add_two_numbers.argtypes = [ctypes.c_int, ctypes.c_int] #Input values
add_two_numbers.restype = ctypes.c_int #Output value

#Now uses
add_two_numbers(20,30)
