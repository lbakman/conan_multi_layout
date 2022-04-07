#include "MyPackage/LibCSystem.h"
#include "LibA.h"
#include "LibC.h"
#include <iostream>

namespace MyPackage {

const char *LibCSystem::name() const
{
	return "LibB";
}

void LibCSystem::initialize(Poco::Util::Application&)
{
	std::cout << "Initialising LibC subsystem" << std::endl;
	LibA(); // Just to illustrate dependencies between components
	LibC();
}

void LibCSystem::uninitialize()
{
	std::cout << "un-initialising LibC subsystem" << std::endl;
}

}
