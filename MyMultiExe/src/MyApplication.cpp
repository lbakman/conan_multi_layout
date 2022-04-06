#include "MyApplication.h"
#include "MyPackage/LibASystem.h"
#include <iostream>

MyApplication::MyApplication()
{
	addSubsystem(new MyPackage::LibASystem());
}

MyApplication::~MyApplication() = default;

void MyApplication::initialize(Poco::Util::Application &self)
{
	std::cout << "Initialising MyApplication" << std::endl;
	Application::initialize(self);
}

void MyApplication::uninitialize()
{
	Application::uninitialize();
	std::cout << "Un-initialising MyApplication" << std::endl;
}

