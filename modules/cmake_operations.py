import ctypes
import os


archive_folder = os.path.dirname(__file__)

library = ctypes.CDLL(f"{archive_folder}\\cmake_operations\\build\\Debug\\cmake-tests.dll")

library.hello()

