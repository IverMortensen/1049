from math import sqrt

# Exercise 1
def Exercise1(message):
	""" Print a message """
	print(message)


# Exercise 2
def Exercise2(value: float):
	""" Calculte absolute value """
	absValue = abs(value)
	print(f"The absolute value of {value} is {absValue}")


# Exercise 3
def Exercise3(age):
	""" Calculate bus ticket from age """
	if age < 18:
		print("20kr")
	elif age < 76:
		print("40kr")
	else:
		print("30kr")


# Exercise 4
def Exercise4(x1, y1, x2, y2):
	""" Calculate distance between two points """
	d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
	print(d)


# Exercise 5
def Exercise5(initVel, acc, time):
	""" Calculate velocity at given time """
	velocity = initVel + (acc * time)
	print(f"{velocity} m/s")


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

