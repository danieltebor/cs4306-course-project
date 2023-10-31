cmake_minimum_required(VERSION 3.10)
project(cs4306-course-project)

set(CMAKE_CXX_STANDARD 17)

add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/bin
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_BINARY_DIR}/bin
    COMMENT "Creating bin directory"
)
add_custom_target(CreateBinDir ALL DEPENDS ${CMAKE_BINARY_DIR}/bin)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_subdirectory(src)