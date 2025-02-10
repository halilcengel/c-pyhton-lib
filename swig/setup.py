from setuptools import setup, Extension

# SWIG interface dosyasından extension modülü oluştur
calculator_module = Extension(
    name='_calculator',  # Başındaki _ önemli
    sources=['calculator.i', 'math.cpp'],
    swig_opts=['-c++'],
    include_dirs=['.']
)

setup(
    name='calculator',
    version='1.0',
    ext_modules=[calculator_module],
    py_modules=['calculator'],
)
