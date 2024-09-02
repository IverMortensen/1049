from math import sqrt, cos, sin

def Exercise1(message):
	""" Print a message """
	print(message)

def Exercise2(value: float):
	""" Calculte absolute value """
	absValue = abs(value)
	print(f"The absolute value of {value} is {absValue}")

def Exercise3(age):
	""" Calculate bus ticket from age """
	if age < 18:
		print("20kr")
	elif age < 76:
		print("40kr")
	else:
		print("30kr")

def Exercise4(x1, y1, x2, y2):
	""" Calculate distance between two points """
	d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
	print(d)

def Exercise5(initVel, acc, time):
	""" Calculate velocity at given time """
	velocity = initVel + (acc * time)
	print(f"{velocity} m/s")


def Exercise6(number):
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

def Exercise7(a, b):
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

def Exercise8(a, b, c):
	""" Sort values in acending order. """
	if a > c:
		a, c = Swap(a, c)

	if a > b:
		a, b = Swap(a, b)
	
	if b > c:
		b, c = Swap(b, c)
	
	print(f"{a}, {b}, {c}")

def Exercise9():
	for num in range(51):
		Exercise1(num)

def Cotangent(k):
	""" Calculates the cotagent of k. """
	return cos(k)/sin(k)

def Exercise10_1(iterations=40):
	""" Calculates the sum cotangent from 1 to set interations, using a for loop."""
	result = sum(Cotangent(k) for k in range(1, iterations+1))
	print(round(result, 2))

def Exercise10_2(iterations=40):
	""" Calculates the sum cotangent from 1 to set interations, using a while loop. """
	result = 0

	while iterations:
		result += Cotangent(iterations)
		iterations -= 1
	print(round(result, 2))

if __name__ == '__main__':
	print("\n--- Exercise 1 ---")
	Exercise1("Hello!")

	print("\n--- Exercise 2 ---")
	Exercise2(4.5)
	Exercise2(-4.5)

	print("\n--- Exercise 3 ---")
	Exercise3(14)
	Exercise3(30)
	Exercise3(80)

	print("\n--- Exercise 4 ---")
	Exercise4(2, 2, -3, -1)

	print("\n--- Exercise 5 ---")
	Exercise5(5, 2, 0)
	Exercise5(5, 2, 4)
	Exercise5(5, 2, 9.5)

	print("\n--- Exercise 6 ---")
	Exercise6(1)
	Exercise6(7)
	Exercise6(14)
	Exercise6(29)

	print("\n--- Exercise 7 ---")
	Exercise7(3, 5)
	Exercise7(7, 1)
	Exercise7(12, 12)

	print("\n--- Exercise 8 ---")
	Exercise8(2, 4, 6)
	Exercise8(9, 2, 1)
	Exercise8(8, 16, 3)
	Exercise8(1, 12, 1)

	print("\n--- Exercise 9 ---")
	Exercise9()
	
	print("\n--- Exercise 10 ---")
	Exercise10_1()
	Exercise10_2()

