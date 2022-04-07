#include "MyPackage/LibBSystem.h"
#include "LibA.h"
#include "LibB.h"
#include <iostream>

namespace MyPackage {

const char *LibBSystem::name() const
{
	return "LibB";
}

void LibBSystem::initialize(Poco::Util::Application&)
{
	std::cout << "Initialising LibB subsystem" << std::endl;
	LibA(); // Just to illustrate dependencies between components
	LibB();
}

void LibBSystem::uninitialize()
{
	std::cout << "un-initialising LibB subsystem" << std::endl;
}

}
