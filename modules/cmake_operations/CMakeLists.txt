#Set the version of cmake
cmake_minimum_required(VERSION 3.24)

#Set the name of the project and the name
project(cmake-tests VERSION 1.0.0)

#Set the compilation version
set (CMAKE_CXX_STANDARD 17)

#Create Shared Library
add_library(${PROJECT_NAME} SHARED
				main.cpp
				main.hpp)


target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)