cmake_minimum_required(VERSION 3.11)
project(NextDateTest)
enable_language(C CXX)
find_package(GTest REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS} src)
add_library(nextdate_lib src/nextdate.cpp)
add_executable(test_nextdate test/test_nextdate_from_csv.cc test/test_nextdate_pict.cc test/test_nextdate.cc)
target_link_libraries(test_nextdate
    PRIVATE
        nextdate_lib
        GTest::GTest
        GTest::Main
)

enable_testing()
add_test(NAME NextDateTests COMMAND test_nextdate)