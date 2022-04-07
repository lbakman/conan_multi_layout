
find_package(Poco REQUIRED Foundation Util)

file(GLOB HEADERS src/*.h)
file(GLOB SOURCES src/*.cpp)
file(GLOB_RECURSE PUBLIC_HEADERS include/*.h ${CMAKE_CURRENT_BINARY_DIR}/include/*.h)

add_library(LibB STATIC ${SOURCES} ${HEADERS} ${PUBLIC_HEADERS})
target_include_directories(LibB
        PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/include>
        PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        )

target_link_libraries(LibB PUBLIC Poco::Util LibA)

install(TARGETS LibB)
install(
        DIRECTORY include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
