file(GLOB SOURCES "*.cpp")

add_library(cs4306-course-project SHARED ${SOURCES})
set_target_properties(cs4306-course-project PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/lib"
    SUFFIX ".dll")