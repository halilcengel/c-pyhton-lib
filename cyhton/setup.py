from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension(
    "calculator",
    sources=["calculator.pyx"],
    include_dirs=["."],
    language="c++"
)

setup(
    name="calculator",
    ext_modules=cythonize([ext]),
    zip_safe=False,
)