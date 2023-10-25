file(GLOB SOURCES "*.cpp")

include_directories(${CMAKE_SOURCE_DIR}/include)

add_library(${PROJECT_NAME} SHARED ${SOURCES})
set_target_properties(${PROJECT_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/lib"
    SUFFIX ".dll")