#!/bin/bash

set -e
set -x

rm -rf MyMultiExe/cmake-build-release

mkdir MyMultiExe/cmake-build-release
pushd MyMultiExe/cmake-build-release
conan install ..
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=conan/conan_toolchain.cmake
cmake --build .
./myexe
popd

