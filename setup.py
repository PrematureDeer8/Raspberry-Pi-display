from setuptools import setup, Extension

setup(
    ext_modules=[Extension("cmult", ["cmult.cpp"],),],
)