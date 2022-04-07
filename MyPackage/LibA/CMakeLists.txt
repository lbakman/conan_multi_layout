
find_package(Poco REQUIRED Foundation Util)

configure_file(Config.h.in "${CMAKE_CURRENT_BINARY_DIR}/include/MyPackage/Config.h" @ONLY)

file(GLOB HEADERS src/*.h)
file(GLOB SOURCES src/*.cpp)
file(GLOB_RECURSE PUBLIC_HEADERS include/*.h ${CMAKE_CURRENT_BINARY_DIR}/include/*.h)

add_library(LibA STATIC ${SOURCES} ${HEADERS} ${PUBLIC_HEADERS})
target_include_directories(LibA
        PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/include>
        PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        )

target_link_libraries(LibA PUBLIC Poco::Util)

install(TARGETS LibA)
install(
        DIRECTORY include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
install(
        DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
