#!/bin/bash

set -e
set -x

rm -rf MyPackage/cmake-build-release
rm -rf MyMultiExe/cmake-build-release

conan editable add MyPackage/ MyPackage/0.1@user/channel

pushd MyPackage
conan install .
pushd cmake-build-release
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=conan/conan_toolchain.cmake
cmake --build . # --target install
popd
popd

mkdir MyMultiExe/cmake-build-release
pushd MyMultiExe/cmake-build-release
conan install ..
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=conan/conan_toolchain.cmake
cmake --build .
./myexe
popd

conan editable remove MyPackage/0.1@user/channel

