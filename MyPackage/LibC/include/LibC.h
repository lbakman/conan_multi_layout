#pragma once

#ifdef _WIN32
  #define LibC_EXPORT __declspec(dllexport)
#else
  #define LibC_EXPORT
#endif

LibC_EXPORT void LibC();
