import math

# --- Exercise 1 ---
def f(x):
    """ Function for f(x). """
    return (math.sin(x) * math.sqrt(abs(x))) / (x * x + 1)

def mapValues(numValues, start, end):
    """
    Makes a list containing values between start and end where
    numValues is the number of values in the list.
    """
    # Calculate the size between each value
    stepSize = (end - start) / (numValues - 1)

    # Add each value to the list
    values = []
    for i in range(numValues):
        values.append(start + i * stepSize)

    # Return the list
    return values


# --- Exercise 2 ---
def f_der(f, x, h=1e-5):
    """ Estimates f'(x) using finite difference method. """
    return (f(x + h) - f(x - h)) / (h*2)


if __name__ == '__main__':
    # Exercise 1
    # Get values for x
    x_vals = mapValues(200, -10 * math.pi, 10 * math.pi)

    # Calculate f(x) for each value of x
    f_vals = []
    for x in x_vals:
        f_vals.append(f(x))

    # Exercise 2
    # Calculate f'(x) for each value of x
    fder_vals = []
    for x in x_vals:
        fder_vals.append(f_der(f, x))
    print(fder_vals)