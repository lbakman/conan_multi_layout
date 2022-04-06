#ifndef MYPROJECT_LIBCSYSTEM_H
#define MYPROJECT_LIBCSYSTEM_H

#include "Poco/Util/Subsystem.h"

namespace MyPackage {

class LibCSystem final : public Poco::Util::Subsystem
{
public:
	LibCSystem() = default;
	~LibCSystem() override = default;

	const char *name() const override;

	void initialize(Poco::Util::Application &app) override;
	void uninitialize() override;
};

}

#endif //MYPROJECT_LIBSYSTEM_H
