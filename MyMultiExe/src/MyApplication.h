#ifndef MYEXE_MYAPPLICATION_H
#define MYEXE_MYAPPLICATION_H

#include "Poco/Util/Application.h"

class MyApplication final : public Poco::Util::Application
{
public:
	MyApplication();
	~MyApplication() override;

private:
	void initialize(Application& self) override;
	void uninitialize() override;
};


#endif //MYEXE_MYAPPLICATION_H
