#include <pybind11/pybind11.h>
#include "../math.hpp"

namespace py = pybind11;

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin";

    py::class_<Calculator>(m, "Calculator")
        .def(py::init<>())
        .def("add", &Calculator::add)
        .def("multiply", &Calculator::multiply);
}
