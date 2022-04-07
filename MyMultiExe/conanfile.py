from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout


class MyMultiExeConan(ConanFile):
    name = "myexe"
    version = "0.1"

    requires = (
        "MyPackage/0.1@user/channel"
    )

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Myexe here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "cmake/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        # This generates "foo-config.cmake" and "bar-config.cmake" in self.generators_folder
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(variables={"CMAKE_ENABLE_CONAN": "OFF"})
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
