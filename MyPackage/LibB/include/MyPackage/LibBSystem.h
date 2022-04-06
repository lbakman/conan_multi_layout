#ifndef MYPROJECT_LIBBSYSTEM_H
#define MYPROJECT_LIBBSYSTEM_H

#include "Poco/Util/Subsystem.h"

namespace MyPackage {

class LibBSystem final : public Poco::Util::Subsystem
{
public:
	LibBSystem() = default;
	~LibBSystem() override = default;

	const char *name() const override;

	void initialize(Poco::Util::Application &app) override;
	void uninitialize() override;
};

}

#endif //MYPROJECT_LIBBSYSTEM_H
