#ifndef MYPROJECT_LIBASYSTEM_H
#define MYPROJECT_LIBASYSTEM_H

#include "Poco/Util/Subsystem.h"

namespace MyPackage {

class LibASystem final : public Poco::Util::Subsystem
{
public:
	LibASystem() = default;
	~LibASystem() override = default;

	const char *name() const override;

	void initialize(Poco::Util::Application &app) override;
	void uninitialize() override;

};

}

#endif //MYPROJECT_LIBASYSTEM_H
