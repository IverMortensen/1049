import math

# --- Exercise 1 ---
def PrintParityAndMod7(number):
    """
    Checks if a nubmer is even or odd
    and if it is divisible by 7.
    """
    if number % 2:
        parity = "odd"
    else:
        parity = "even"

    if number % 7:
        is_isnot = "is not"
    else:
        is_isnot = "is"

    print(f"{number} is {parity} and {is_isnot} divisible by 7.")


# --- Exercise 2 ---
def PrintAbsoluteDifference(a, b):
    """ Calculate the absolute difference between a and b. """
    if a > b:
        difference = a - b
    elif b > a:
        difference = b - a
    else:
        difference = 0

    print(f"The absolute difference between {a} and {b} is {difference}.")


# --- Exercise 3 ---
def Swap(a, b):
    """ Swap two numbers. """
    return b, a

def LargestValue(a, b, c):
    """ Returns the largest value. """
    if a > b and a > c:
        return a

    elif b > c:
        return b

    else:
        return c
    
def SmallestValue(a, b, c):
    """ Returns the smallest value. """
    if a < b and a < c:
        return a

    elif b < c:
        return b

    else:
        return c

# Exercise 3a
def PrintLargestValue(a, b, c):
    """ Prints the largest value. """
    largestValue = LargestValue(a, b, c)
    print(f"{largestValue} is the largest value of {a}, {b} and {c}.")

# Exercise 3b
def SwapLargestAndSmallestValue(a, b, c):
    """ Swaps the largest and smallest value and prints the result. """
    largestValue = LargestValue(a, b, c)
    smallestValue = SmallestValue(a, b, c)
    print(f"Swapping largest and smallest value of {a}, {b} and {c}", end=" ")

    if a is largestValue:
        if b is smallestValue:
            a, b = Swap(a, b)
        else:
            a, c = Swap(a, c)

    elif b is largestValue:
        if a is smallestValue:
            b, a = Swap(b, a)
        else:
            b, c = Swap(b, c)

    elif c is largestValue:
        if a is smallestValue:
            c, a = Swap(c, a)
        else:
            c, b = Swap(c, b)

    print(f"gives {a}, {b} and {c}.")

# Exercise 3c
def PrintAscendingOrder(a, b, c):
    """ Sorts values in acending order. """
    print(f"{a}, {b} and {c} in ascendig order is", end=" ")
    if a > c:
        a, c = Swap(a, c)

    if a > b:
        a, b = Swap(a, b)
    
    if b > c:
        b, c = Swap(b, c)
    
    print(f"{a}, {b}, {c}")


# --- Exercise 4 ---
def PrintParityAndMod7Range(start=0, stop=51):
    for num in range(start, stop):
        PrintParityAndMod7(num)


# --- Exercise 5 ---
def Cotangent(k):
    """ Calculates the cotagent of k. """
    return math.cos(k)/math.sin(k)

# Exercise 5a
def PrintCotagentUsingForLoop(iterations=40):
    """
    Calculates the sum cotangent from 1
    to set interations, using a for loop.
    """
    result = sum(Cotangent(k) for k in range(1, iterations+1))
    print(f"Cotangent using for loop: \t{round(result, 2)}")

# Exercise 5b
def PrintCotagentUsingWhileLoop(iterations=40):
    """
    Calculates the sum cotangent from 1
    to set interations, using a while loop.
    """
    result = 0

    while iterations:
        result += Cotangent(iterations)
        iterations -= 1
    print(f"Cotangent using while loop: \t{round(result, 2)}")


if __name__ == "__main__":
    # Exercise 1
    print("\n--- Exercise 1 ---")
    PrintParityAndMod7(1)
    PrintParityAndMod7(7)
    PrintParityAndMod7(30)

    # Exercise 2
    print("\n--- Exercise 2 ---")
    PrintAbsoluteDifference(3, 5)
    PrintAbsoluteDifference(7, 1)
    PrintAbsoluteDifference(12, 12)

    # Exercise 3a
    print("\n--- Exercise 3a ---")
    PrintLargestValue(1, 2, 3)
    PrintLargestValue(9, 2, 0)
    PrintLargestValue(-8, 7, 2)

    # Exercise 3b
    print("\n--- Exercise 3b ---")
    SwapLargestAndSmallestValue(1, 6, 7)
    SwapLargestAndSmallestValue(13, 2, 4)
    SwapLargestAndSmallestValue(12, 43, -2)

    # Exercise 3c
    print("\n--- Exercise 3c ---")
    PrintAscendingOrder(2, 4, 6)
    PrintAscendingOrder(9, 2, 1)
    PrintAscendingOrder(3, 12, 3)

    # Exercise 4
    print("\n--- Exercise 4 ---")
    PrintParityAndMod7Range(0, 51)

    # Exercise 5a
    print("\n--- Exercise 5a ---")
    PrintCotagentUsingForLoop()

    # Exercise 5b
    print("\n--- Exercise 5a ---")
    PrintCotagentUsingWhileLoop()
