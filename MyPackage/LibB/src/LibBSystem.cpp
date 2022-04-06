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
	LibA();
	LibB();
	std::cout << "Initialising LibB subsystem" << std::endl;
}

void LibBSystem::uninitialize()
{
	std::cout << "un-initialising LibB subsystem" << std::endl;
}

}
