#pragma once

class Calculator {
public:
    Calculator() = default;

    double add(double a, double b) {
        return a + b;
    }

    double multiply(double a, double b) {
        return a * b;
    }
};