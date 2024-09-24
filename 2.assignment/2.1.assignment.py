# --- Exersice 1 ---
def largest(a, b, c):
    """ Returns the largest number. """
    if a > b and a > c:
        return a

    elif b > c:
        return b

    else:
        return c

# --- Exercise 2 ---
def QuadraticEquation(x):
    return 2 * x * x - x

def BisectionAlgorithm(a, b, f):
    """
    Returns the estimated root between f(a) and f(b).
    f(a) needs to be greater than 0
    f(b) needs to be less than 0
    """
    if f(a) < 0:
        print(f"f(a) isn't greater than 0.")
    if f(b) > 0:
        print(f"f(b) isn't less than 0.")

    # Find the midpoint
    m = (a + b) / 2
    f_of_m = f(m)

    # Check if f(m) is close to 0
    if not round(f_of_m, 2):
        return m
    
    # Check if f(m) is over or under 0,
    # replacing a if over, and b if under
    # and running the algorithim again.
    if f_of_m > 0:
        result = BisectionAlgorithm(m, b, f)
    else:
        result = BisectionAlgorithm(a, m, f)
    
    return result

# --- Exercise 3 ---
def busiest_month(fileName: str):
    """
    Prints the month with the highest number of births.
    """
    highestNumBirths = 0
    busiestMonth = None
    year = fileName.split('/')[-1].split('.')[0]

    # Open file
    with open(fileName) as file:
        # Go through each line
        for line in file:
            # Get the month and number of births
            month, numBirths = line.split(" ")
            numBirths = int(numBirths)

            # Update the busiest month
            if numBirths > highestNumBirths:
                busiestMonth = month
                highestNumBirths = numBirths

    print(f"Busiest month {year}: {busiestMonth}")

def yearly_average(fileName: str):
    """
    Prints the monthly average number of births of a year.
    """
    totalBirths = 0
    numMonths = 0
    year = fileName.split('/')[-1].split('.')[0]

    # Open file
    with open(fileName) as file:
        # Go through each line
        for line in file:
            numMonths += 1

            # Get the month and number of births
            month, numBirths = line.split(" ")
            numBirths = int(numBirths)

            totalBirths += numBirths

    averageBirths = round(totalBirths / numMonths)
    print(f"Average births {year}: {averageBirths}")

if __name__ == "__main__":
    # Exercise 1
    print("--- Exercise 1 ---")
    a, b, c = 1, 2, 3
    largestNumber = largest(a, b, c)
    print(f"Largest number of {a}, {b}, {c} is {largestNumber}")

    a, b, c = 10, -12, 6
    largestNumber = largest(a, b, c)
    print(f"Largest number of {a}, {b}, {c} is {largestNumber}")

    # Exercise 2
    print("\n--- Exercise 2 ---")
    root1 = BisectionAlgorithm(1, 0.25, QuadraticEquation)
    root2 = BisectionAlgorithm(-1, 0.25, QuadraticEquation)
    print(f"{round(root1,2)} is a root")
    print(f"{round(root2,2)} is a root")

    # Exercise 3
    print("\n--- Exercise 3a ---")
    busiest_month("./2.1.datafiles/2018.txt")
    busiest_month("./2.1.datafiles/2019.txt")
    busiest_month("./2.1.datafiles/2020.txt")

    print("\n--- Exercise 3b ---")
    yearly_average("./2.1.datafiles/2018.txt")
    yearly_average("./2.1.datafiles/2019.txt")
    yearly_average("./2.1.datafiles/2020.txt")
