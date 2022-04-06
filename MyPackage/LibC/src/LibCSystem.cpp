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
	LibA();
	LibC();
	std::cout << "Initialising LibC subsystem" << std::endl;
}

void LibCSystem::uninitialize()
{
	std::cout << "un-initialising LibC subsystem" << std::endl;
}

}
