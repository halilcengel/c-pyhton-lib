cdef extern from "../math.hpp":
    cdef cppclass Calculator:
        Calculator() except +
        double add(double a, double b)
        double multiply(double a, double b)