file(GLOB SOURCES "*.cpp")

list(APPEND CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/lib/oneTBB")

find_package(TBB REQUIRED)

include_directories(${CMAKE_SOURCE_DIR}/include)

add_library(lib_eight_puzzle_solver SHARED ${SOURCES})
target_link_libraries(lib_eight_puzzle_solver PRIVATE TBB::tbb)
set_target_properties(lib_eight_puzzle_solver PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/lib"
    LIBRARY_OUTPUT_NAME "_eight_puzzle_solver"
    SUFFIX ".dll")