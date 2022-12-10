cmake_minimum_required(VERSION 3.24)

project(_quine_mccluskey_tomas789)

include(FetchContent)

FetchContent_Declare(
  pybind11
  URL https://codeload.github.com/pybind/pybind11/tar.gz/refs/tags/v2.10.1
  DOWNLOAD_EXTRACT_TIMESTAMP 1)
FetchContent_Populate(pybind11)
message(STATUS "pybind11 is available in " ${pybind11_SOURCE_DIR})

find_package(Python COMPONENTS Interpreter Development)
add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})

# Python method:
pybind11_add_module(_quine_mccluskey_tomas789 src_cpp/qmc.cpp)
target_link_libraries(_quine_mccluskey_tomas789 PRIVATE pybind11::headers)
target_compile_features(_quine_mccluskey_tomas789 PRIVATE cxx_std_17)
