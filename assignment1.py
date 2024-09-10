from math import sqrt, cos, sin

# Exercise 1.1
def Exercise1_1(message):
	""" Print a message """
	print(message)


# Exercise 1.2
def Exercise1_2(value: float):
	""" Calculte absolute value """
	absValue = abs(value)
	print(f"The absolute value of {value} is {absValue}")


# Exercise 1.3
def Exercise1_3(age):
	""" Calculate bus ticket from age """
	if age < 18:
		print("20kr")
	elif age < 76:
		print("40kr")
	else:
		print("30kr")


# Exercise 1.4
def Exercise1_4(x1, y1, x2, y2):
	""" Calculate distance between two points """
	d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
	print(d)


# Exercise 1.5
def Exercise1_5(initVel, acc, time):
	""" Calculate velocity at given time """
	velocity = initVel + (acc * time)
	print(f"{velocity} m/s")


# Exercise 2.1
def Exercise2_1(number):
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


# Exercise 2.2
def Exercise2_2(a, b):
	""" Calculate the absolute difference between a and b. """
	if a > b:
		difference = a - b
	elif b > a:
		difference = b - a
	else:
		difference = 0

	print(f"The absolute difference between {a} and {b} is {difference}.")


# Exercise 2.3
def Swap(a, b):
	""" Swap two numbers. """
	return b, a

def Exercise2_3(a, b, c):
	""" Sort values in acending order. """
	if a > c:
		a, c = Swap(a, c)

	if a > b:
		a, b = Swap(a, b)
	
	if b > c:
		b, c = Swap(b, c)
	
	print(f"{a}, {b}, {c}")


# Exercise 2.4
def Exercise2_4():
	for num in range(51):
		Exercise1_1(num)


# Exercise 2.5
def Cotangent(k):
	""" Calculates the cotagent of k. """
	return cos(k)/sin(k)

def Exercise2_5a(iterations=40):
	""" Calculates the sum cotangent from 1 to set interations, using a for loop."""
	result = sum(Cotangent(k) for k in range(1, iterations+1))
	print(round(result, 2))

def Exercise2_5b(iterations=40):
	""" Calculates the sum cotangent from 1 to set interations, using a while loop. """
	result = 0

	while iterations:
		result += Cotangent(iterations)
		iterations -= 1
	print(round(result, 2))


if __name__ == '__main__':
	print("\n--- Exercise 1.1 ---")
	Exercise1_1("Hello!")

	print("\n--- Exercise 1.2 ---")
	Exercise1_2(4.5)
	Exercise1_2(-4.5)

	print("\n--- Exercise 1.3 ---")
	Exercise1_3(14)
	Exercise1_3(30)
	Exercise1_3(80)

	print("\n--- Exercise 1.4 ---")
	Exercise1_4(2, 2, -3, -1)

	print("\n--- Exercise 1.5 ---")
	Exercise1_5(5, 2, 0)
	Exercise1_5(5, 2, 4)
	Exercise1_5(5, 2, 9.5)

	print("\n--- Exercise 2.1 ---")
	Exercise2_1(1)
	Exercise2_1(7)
	Exercise2_1(14)
	Exercise2_1(29)

	print("\n--- Exercise 2.2 ---")
	Exercise2_2(3, 5)
	Exercise2_2(7, 1)
	Exercise2_2(12, 12)

	print("\n--- Exercise 2.3 ---")
	Exercise2_3(2, 4, 6)
	Exercise2_3(9, 2, 1)
	Exercise2_3(8, 16, 3)
	Exercise2_3(1, 12, 1)

	print("\n--- Exercise 2.4 ---")
	Exercise2_4()
	
	print("\n--- Exercise 2.5 ---")
	Exercise2_5a()
	Exercise2_5b()

