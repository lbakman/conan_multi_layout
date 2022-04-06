cmake_minimum_required(VERSION 3.15)
# Make sure we can find our custom CMake modules
list(INSERT CMAKE_MODULE_PATH 0 "${CMAKE_SOURCE_DIR}/cmake" "${CMAKE_BINARY_DIR}")
list(INSERT CMAKE_PREFIX_PATH 0 "${CMAKE_BINARY_DIR}/conan" "${CMAKE_BINARY_DIR}")

include(MyConan)

project(mymultiexe CXX)

if(CMAKE_ENABLE_CONAN)
    # Only call conan if we are being built from CMake and not from conan
    conan_cmake_autodetect(settings)
    conan_cmake_install(PATH_OR_REFERENCE ${CMAKE_SOURCE_DIR}
            BUILD missing
            OPTIONS ${CONAN_RUN_OPTIONS}
            SETTINGS ${settings})
endif(CMAKE_ENABLE_CONAN)

find_package(Poco REQUIRED Foundation Util)
find_package(MyPackage REQUIRED LibA)

file(GLOB HEADERS src/*.h)
file(GLOB SOURCES src/*.cpp)

add_executable(myexe ${SOURCES} ${HEADERS})

target_include_directories(myexe
        PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${CMAKE_CURRENT_BINARY_DIR}/src
        )

target_compile_options(myexe
        PRIVATE
        $<$<CXX_COMPILER_ID:GNU>:${PROJECT_GNU_COMPILE_FLAGS}>
        )

target_link_libraries(myexe PRIVATE Poco::Util MyPackage::LibA)

install(TARGETS myexe)
