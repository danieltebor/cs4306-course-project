file(GLOB SOURCES "*.cpp")

include_directories(${CMAKE_SOURCE_DIR}/include)

add_library(lib_eight_puzzle_solver SHARED ${SOURCES})
set_target_properties(lib_eight_puzzle_solver PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/lib"
    LIBRARY_OUTPUT_NAME "_eight_puzzle_solver"
    SUFFIX ".dll")