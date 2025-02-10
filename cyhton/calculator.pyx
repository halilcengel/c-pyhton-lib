from calculator cimport Calculator

cdef class PyCalculator:
    cdef Calculator * c_calc

    def __cinit__(self):
        self.c_calc = new Calculator()

    def __dealloc__(self):
        del self.c_calc

    def add(self, double a, double b):
        return self.c_calc.add(a, b)

    def multiply(self, double a, double b):
        return self.c_calc.multiply(a, b)