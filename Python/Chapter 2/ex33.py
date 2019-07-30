# Regex 1: ([\+-])?\s?(\d*)\s?[*\/]?\s?([a-zA-Z])?(\^\d)?\s? => 5*x^2 + 7*x + 1

"""
    Polynomial in Standard Notation is made by:
        Term
        Term + Term
        Term - Term (Term + -Term)
    Term:
        Coefficent: Constant
        Variable: x
        Exponent: n >= 0
"""

import re


class FirstDerivativePolynomial:
    def __init__(self, string):
        self._expression = string
        self._first_deriv = ""

    def solve(self):
        result = ""
        for sign, coefficient, var, exp in re.findall(
            "([\+-])?\s?(\d*)\s?[*\/]?\s?([a-zA-Z])?(\^\d)?\s?", "+" + self._expression
        ):
            # print(sign, coefficient, var, exp)
            if var != "":
                if coefficient == "":
                    coefficient = "1"
                coefficientInt = int(coefficient)
                if exp == "":
                    expInt = 1
                else:
                    expInt = int(exp.split("^")[1])
                coefficientInt *= expInt
                expInt -= 1
                if expInt == 0:
                    result += sign + " %d " % coefficientInt
                else:
                    if expInt >= 2:
                        result += sign + " %d * x^%d " % (coefficientInt, expInt)
                    else:
                        result += sign + " %d * x " % (coefficientInt)
        if result[0] == "+":
            result = result[2:]
        self._first_deriv = result
        return result

    def get_solve(self):
        return self._first_deriv


if __name__ == "__main__":
    FirstDerivativePolynomial("12*x^6 + 4*x^2 + 3*x^1 - 7*x").solve()
