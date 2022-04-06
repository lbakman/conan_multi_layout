from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout


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
    exports_sources = "CMakeLists.txt", "LibA/*", "LibB/*", "LibC/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)
        self.cpp.build.libdirs = ["lib64"]
        # self.cpp.build.bindirs = ["lib64"]
        self.cpp.build.includedirs = ["include"]

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["CMAKE_ENABLE_CONAN"] = "OFF"
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
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

        # self.cpp_info.components["LibB"].set_property("cmake_target_name", "MyPackage::LibB")
        # self.cpp_info.components["LibB"].libs = ["LibB"]
        # self.cpp_info.components["LibB"].requires = ["LibA", "poco::poco"]
        #
        # self.cpp_info.components["LibC"].set_property("cmake_target_name", "MyPackage::LibC")
        # self.cpp_info.components["LibC"].libs = ["LibC"]
        # self.cpp_info.components["LibC"].requires = ["LibA", "poco::poco"]
