import math

def Exercise1(number):
	""" Check if nubmer is even or odd and is divisible by 7. """
	if number % 2:
		parity = "odd"
	else:
		parity = "even"

	if number % 7:
		is_isnot = "is not"
	else:
		is_isnot = "is"

	print(f"{number} is {parity} and {is_isnot} divisible by 7.")

def Exercise2(a, b):
	""" Calculate the absolute difference between a and b. """
	if a > b:
		difference = a - b
	elif b > a:
		difference = b - a
	else:
		difference = 0

	print(f"The absolute difference between {a} and {b} is {difference}.")

def Swap(a, b):
	""" Swap two numbers. """
	return b, a

def Exercise3(a, b, c):
	""" Sort values in acending order. """
	if a > c:
		a, c = Swap(a, c)

	if a > b:
		a, b = Swap(a, b)
	
	if b > c:
		b, c = Swap(b, c)
	
	print(f"{a}, {b}, {c}")

def Exercise4():
	for num in range(51):
		Exercise1(num)

def Cotangent(k):
	""" Calculates the cotagent of k. """
	return math.cos(k)/math.sin(k)

def Exercise5_1(iterations=40):
	""" Calculates the sum cotangent from 1 to set interations, using a for loop."""
	result = sum(Cotangent(k) for k in range(1, iterations+1))
	print(round(result, 2))

def Exercise5_2(iterations=40):
	""" Calculates the sum cotangent from 1 to set interations, using a while loop. """
	result = 0

	while iterations:
		result += Cotangent(iterations)
		iterations -= 1
	print(round(result, 2))

if __name__ == "__main__":
	print("\n--- Exercise 1 ---")
	Exercise1(1)
	Exercise1(7)
	Exercise1(14)
	Exercise1(29)

	print("\n--- Exercise 2 ---")
	Exercise2(3, 5)
	Exercise2(7, 1)
	Exercise2(12, 12)

	print("\n--- Exercise 3 ---")
	Exercise3(2, 4, 6)
	Exercise3(9, 2, 1)
	Exercise3(8, 16, 3)
	Exercise3(1, 12, 1)

	print("\n--- Exercise 4 ---")
	Exercise4()
	
	print("\n--- Exercise 5 ---")
	Exercise5_1()
	Exercise5_2()
