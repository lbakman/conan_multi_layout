from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
import os


class MyPackageConan(ConanFile):
    name = "MyPackage"
    version = "0.1"

    requires = (
        "poco/1.11.1"
    )

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "LibA/*", "LibB/*", "LibC/*", "cmake/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        # Basing this on the cmake_layout. Don't know if I should use a custom layout to begin with,
        # or even create a cmake_multi_layout.
        cmake_layout(self)

        # The first example here tries to set up paths to where everything is built or generated
        # - without installing it.
        self.cpp.package.components["LibA"].includedirs = ["include"]
        self.cpp.package.components["LibA"].libdirs = ["lib"]
        self.cpp.source.components["LibA"].includedirs = ["LibA/include"]
        # We include the next line, because our project generates an include file to our build folder.
        self.cpp.build.components["LibA"].includedirs = ["LibA/include"]
        self.cpp.build.components["LibA"].libdirs = ["LibA"]

        self.cpp.package.components["LibB"].includedirs = ["include"]
        self.cpp.package.components["LibB"].libdirs = ["lib"]
        self.cpp.source.components["LibB"].includedirs = ["LibB/include"]
        # Not here though, because we get a CMake error that it does not exist.
        # self.cpp.build.components["LibB"].includedirs = ["LibB/include"]
        self.cpp.build.components["LibB"].libdirs = ["LibB"]

        self.cpp.package.components["LibC"].includedirs = ["include"]
        self.cpp.package.components["LibC"].libdirs = ["lib"]
        self.cpp.source.components["LibC"].includedirs = ["LibC/include"]
        # Not here though, because we get a CMake error that it does not exist.
        # self.cpp.build.components["LibC"].includedirs = ["LibC/include"]
        self.cpp.build.components["LibC"].libdirs = ["LibC"]

        # The second example assumes that we perform a CMake install, before using it (in editable mode).
        # In this case, executing a CMake install, will place all files in <CMAKE_BINARY_DIR>/include and
        # <CMAKE_BINARY_DIR>/lib64 (in my case). This is probably the case that I personally would use, because
        # this is what I am used to with editable mode and the previous external layout file.
        # self.cpp.package.libdirs = ["lib"]
        # self.cpp.package.includedirs = ["include"]
        # self.cpp.build.libdirs = ["lib64"]  # I am sure I can determine this automatically - this is an experiment.
        # self.cpp.build.includedirs = ["include"]
        # self.cpp.package.components["LibA"].includedirs = self.cpp.package.includedirs
        # self.cpp.package.components["LibA"].libdirs = self.cpp.package.libdirs
        # self.cpp.build.components["LibA"].includedirs = self.cpp.build.includedirs
        # self.cpp.build.components["LibA"].libdirs = self.cpp.build.libdirs
        #
        # self.cpp.package.components["LibB"].includedirs = self.cpp.package.includedirs
        # self.cpp.package.components["LibB"].libdirs = self.cpp.package.libdirs
        # self.cpp.build.components["LibB"].includedirs = self.cpp.build.includedirs
        # self.cpp.build.components["LibB"].libdirs = self.cpp.build.libdirs
        #
        # self.cpp.package.components["LibC"].includedirs = self.cpp.package.includedirs
        # self.cpp.package.components["LibC"].libdirs = self.cpp.package.libdirs
        # self.cpp.build.components["LibC"].includedirs = self.cpp.build.includedirs
        # self.cpp.build.components["LibC"].libdirs = self.cpp.build.libdirs

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        # Tell CMake NOT to execute conan - in-build.
        cmake.configure(variables={"CMAKE_ENABLE_CONAN": "OFF"})
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "MyPackage")
        self.cpp_info.set_property("cmake_target_name", "MyPackage::MyPackage")

        self.cpp_info.filenames["cmake_find_package"] = "MyPackage"
        self.cpp_info.filenames["cmake_find_package_multi"] = "MyPackage"
        self.cpp_info.names["cmake_find_package"] = "MyPackage"
        self.cpp_info.names["cmake_find_package_multi"] = "MyPackage"

        self.cpp_info.components["LibA"].set_property("cmake_target_name", "MyPackage::LibA")
        self.cpp_info.components["LibA"].libs = ["LibA"]
        self.cpp_info.components["LibA"].requires = ["poco::poco"]

        self.cpp_info.components["LibB"].set_property("cmake_target_name", "MyPackage::LibB")
        self.cpp_info.components["LibB"].libs = ["LibB"]
        self.cpp_info.components["LibB"].requires = ["LibA", "poco::poco"]

        self.cpp_info.components["LibC"].set_property("cmake_target_name", "MyPackage::LibC")
        self.cpp_info.components["LibC"].libs = ["LibC"]
        self.cpp_info.components["LibC"].requires = ["LibA", "poco::poco"]
