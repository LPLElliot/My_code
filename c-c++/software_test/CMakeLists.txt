cmake_minimum_required(VERSION 3.11) 
project(SoftwareTest)

enable_language(C CXX)

include(FetchContent)

FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest
    GIT_TAG        v1.14.0  
)

FetchContent_MakeAvailable(googletest)

enable_testing()

add_subdirectory(test1)