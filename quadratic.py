# Replace the "ANSWER HERE" for your answer

import math
def roots(a, b, c):
    if ((b**2) - (4*a*c)) >= 0:
        discr = b**2 - (4*a*c)
        r1 = (((-b) + math.sqrt(discr)) / (2 * a))
        r2 = (((-b) - math.sqrt(discr)) / (2 * a))
        if r1 != r2:
            return f"({r1}, {r2})"
        elif r1 == r2:
            return f"({r1})"
    else:
        return "( )"



def value_y(a, b, c, x):
    y= a*(x**2) + b*x + c
    return y


def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b!=0 and c != 0:
        return f"f(x) = {b} * X + {c}"
    elif a == 0 and b == 0 and c != 0:
        return f"f(x) = {c}"
    elif a != 0 and b == 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a != 0 and b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif a != 0 and b != 0 and c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a == 0 and b == 0 and c == 0:
        return f"f(x) = 0"


def derivation(a, b, c):
    if (2 * a) !=  0 and b!= 0:
        return f"f'(x) = {(2*a)} * X + {b}"
    elif (2 * a) == 0 and b!= 0:
        return f"f'(x) = {b}"
    elif (2 * a) != 0 and b== 0:
        return f"f'(x) = {2 * a} * X"
    elif (2 * a) == 0 and b == 0:
        return f"f'(x) = 0"
