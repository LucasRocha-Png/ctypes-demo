#Set the version of cmake
cmake_minimum_required(VERSION 3.22)

#Set the name of the project and the name
project(cmake-tests VERSION 1.0.0)


set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror -std=c++17")

#Config the compiler to compile in c++ std 17				
set (CMAKE_CXX_STANDARD 17)

#Imports the subdirectory folder of print vector
add_subdirectory(print_vector)

#Create Shared Library of main
add_library(${PROJECT_NAME} SHARED
				main.cpp
				main.hpp)

#Links print_vector library to the project
target_link_libraries(${PROJECT_NAME}
					  print_vector) 

#Config the compiler to compile in c++ std 17					  				  
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
