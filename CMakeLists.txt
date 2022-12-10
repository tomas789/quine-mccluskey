cmake_minimum_required(VERSION 3.23)

project(_quine_mccluskey_tomas789)

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

# Python method:
pybind11_add_module(_quine_mccluskey_tomas789 src_cpp/qmc.cpp)
target_link_libraries(_quine_mccluskey_tomas789 PRIVATE pybind11::headers)
target_compile_features(_quine_mccluskey_tomas789 PRIVATE cxx_std_17)
