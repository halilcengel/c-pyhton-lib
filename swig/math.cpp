#include "math.hpp"

cmake_minimum_required(VERSION 3.10)
project(Calculator)

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_PATH})


set_source_files_properties(calculator.i PROPERTIES CPLUSPLUS ON)
swig_add_library(calculator
    LANGUAGE python
    SOURCES calculator.i math.cpp)
swig_link_libraries(calculator ${PYTHON_LIBRARIES})