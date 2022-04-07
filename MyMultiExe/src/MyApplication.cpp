#include "MyApplication.h"
#include "MyPackage/LibASystem.h"
#include "MyPackage/LibBSystem.h"
#include "MyPackage/LibCSystem.h"
#include <iostream>

MyApplication::MyApplication()
{
	addSubsystem(new MyPackage::LibASystem());
	addSubsystem(new MyPackage::LibBSystem());
	addSubsystem(new MyPackage::LibCSystem());
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

