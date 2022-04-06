# Make sure we only include this file once.
if(DEFINED __INCLUDED_MY_CONAN_CMAKE)
    return()
endif()
set(__INCLUDED_MY_CONAN_CMAKE TRUE)

option(CMAKE_ENABLE_CONAN  "Enable support for Conan within CMake" ON)
if(CMAKE_ENABLE_CONAN)
    # Download automatically, you can also just copy the conan.cmake file
    if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
        message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
        file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/0.18.1/conan.cmake"
                "${CMAKE_BINARY_DIR}/conan.cmake" TLS_VERIFY ON)
    endif()

    include(${CMAKE_BINARY_DIR}/conan.cmake)
endif(CMAKE_ENABLE_CONAN)
