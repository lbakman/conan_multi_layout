#pragma once

#ifdef _WIN32
  #define LibA_EXPORT __declspec(dllexport)
#else
  #define LibA_EXPORT
#endif

LibA_EXPORT void LibA();
