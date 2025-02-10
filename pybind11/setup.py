from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "example",
        ["bindings.cpp"],
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name="example",
    ext_modules=ext_modules,
    setup_requires=["pybind11>=2.2.0"],
    zip_safe=False,
)

#python setup.py build_ext --inplace