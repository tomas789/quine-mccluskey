cmake_minimum_required(VERSION 3.23)

project(qmc)

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)

# Python method:
pybind11_add_module(_qmc src/qmc.cpp)
target_link_libraries(_qmc PRIVATE pybind11::headers)
target_compile_features(_qmc PRIVATE cxx_std_17)
