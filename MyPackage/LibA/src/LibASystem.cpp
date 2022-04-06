#include "MyPackage/LibASystem.h"
#include "LibA.h"
#include <iostream>

namespace MyPackage {

const char *LibASystem::name() const
{
	return "LibA";
}

void LibASystem::initialize(Poco::Util::Application&)
{
	LibA();
	std::cout << "Initialising LibA subsystem" << std::endl;
}

void LibASystem::uninitialize()
{
	std::cout << "un-initialising LibA subsystem" << std::endl;
}

}
