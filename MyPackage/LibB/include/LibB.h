#pragma once

#ifdef _WIN32
  #define LibB_EXPORT __declspec(dllexport)
#else
  #define LibB_EXPORT
#endif

LibB_EXPORT void LibB();
