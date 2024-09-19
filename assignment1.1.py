from math import sqrt

# Exercise 1
def PrintVariable(variable):
	""" Print a variable """
	print(variable)


# Exercise 2
def PrintAbsoluteValue(value: float):
	""" Calculte absolute value """
	absValue = abs(value)
	print(f"The absolute value of {value} is {absValue}")


# Exercise 3
def PrintBusTicketPrice(age: int):
	""" Calculates bus ticket from age """
	price = 0

	if age < 18:
		price = 20
	elif age < 76:
		price = 40
	else:
		price = 30
	
	print(f"Bus ticket for a {age}-year-old costs {price}kr.")


# Exercise 4
def PrintDistance(x1, y1, x2, y2):
	""" Calculates distance between two points """
	distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
	print(f"Distance between {x1}, {y1} and {x2}, {y2} is {distance}.")


# Exercise 5
def PrintVelocity(initVel, acc, time):
	""" Calculates velocity at given time """
	velocity = initVel + (acc * time)
	print(f"Velocity at time {time} is {velocity} m/s.")


if __name__ == '__main__':
	# Exercise 1
	print("\n--- Exercise 1 ---")
	PrintVariable("Hello!")

	# Exercise 2
	print("\n--- Exercise 2 ---")
	PrintAbsoluteValue(4.5)
	PrintAbsoluteValue(-4.5)

	# Exercise 3
	print("\n--- Exercise 3 ---")
	PrintBusTicketPrice(14)
	PrintBusTicketPrice(30)
	PrintBusTicketPrice(80)

	# Exercise 4
	print("\n--- Exercise 4 ---")
	PrintDistance(2, 2, -3, -1)

	# Exercise 5
	print("\n--- Exercise 5 ---")
	PrintVelocity(5, 2, 0)
	PrintVelocity(5, 2, 4)
	PrintVelocity(5, 2, 9.5)

