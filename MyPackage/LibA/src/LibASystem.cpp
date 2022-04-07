#include "MyPackage/LibASystem.h"
#include "MyPackage/Config.h"
#include "LibA.h"
#include <iostream>

namespace MyPackage {

const char *LibASystem::name() const
{
	return "LibA";
}

void LibASystem::initialize(Poco::Util::Application&)
{
	std::cout << "Initialising LibA subsystem" << std::endl;
	std::cout << "- Config: " << MY_CONFIG_OPTION << std::endl;
	LibA();
}

void LibASystem::uninitialize()
{
	std::cout << "un-initialising LibA subsystem" << std::endl;
}

}
