# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x>=y:
        return x
    else:
        return y


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if (x>=y and x>z) or (x>y and x>=z):
        return x
    elif (y>=x and y>z) or (y>x and y>=z):
        return y
    elif (z>=x and z>y) or (z>x and z>=y):
        return z
    elif x==y==z:
        return x
