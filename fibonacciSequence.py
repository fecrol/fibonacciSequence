import math


def menu():
	"""
	Presents the user with 4 options:
	- Print a Fibonacci Sequence up to nth number.
	- Print the nth Fibonacci number.
	- Check if a number is a Fibonacci number.
	- Quit the program.
	"""

	while True:
		try:
			print("\nEnter 1 to print a Fibonacci Sequence")
			print("Enter 2 to print nth number from the Fibonacci Sequence")
			print("Enter 3 to check if a number is part of the Fibonacci Sequence")
			print("Enter 4 to quit")
			choice = int(input("Enter: "))

			# While input is not 1 or 2, keeps prompting for a valid input
			while choice not in [1, 2, 3, 4]:
				print("\nInvalid input, please try again")
				print("\nEnter 1 to print a Fibonacci Sequence")
				print("Enter 2 to print nth number from the Fibonacci Sequence")
				print("Enter 3 to check if a number is part of the Fibonacci Sequence")
				print("Enter 4 to quit")
				choice = int(input("Enter: "))
			return choice
		# If value entered is anything but an integer, displays a warning message
		except ValueError:
			print("\nInvalid input, please try again")


# Prompts the user to enter a number to which to generate the Fibonacci Sequence
def user_number():
	"""
	Prompts the user to enter a number up to which to generate a Fibonacci sequence, which number from the Fibonacci
	sequence to display or to check whether provided number is a Fibonacci number.
	"""

	while True:
		try:
			num = int(input("\nEnter a positive integer: "))

			# While input is less than or equal to 0, keeps prompting for a valid input
			while num < 0:
				print("\nInvalid input, please try again")
				num = int(input("Enter a positive integer: "))
			return num
		# If value entered is anything but an integer, displays a warning message
		except ValueError:
			print("\nInvalid input, please try again")


def fibonacci_sequence(n):
	"""
	Returns the Fibonacci Sequence up to and including number specified by the user
	"""

	# The first two numbers in the sequence
	sequence = [0, 1]

	# Returns the first number in the sequence
	if n == 0:
		return sequence[:1]
	# Returns the first two numbers in the sequence
	elif n == 1:
		return sequence
	# Otherwise returns the first n numbers in the sequence
	else:
		# n - 1 in order to return n numbers in the sequence as there are already 2 numbers
		for i in range(1, n):
			# Grabs the number at index i and adds it to the previous number. Appends result to the sequence
			sequence.append(sequence[i] + sequence[i - 1])
		return sequence


def fibonacci_number(n):
	"""
	Returns the nth number from the Fibonacci Sequence
	"""

	# Fn = (((1 + sqrt(5)) / 2)^n - ((1 - sqrt(5)) / 2)^n) / sqrt(5)
	return int((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5))


def is_number_fibonacci(n):
	"""
	Returns whether a number is part of the Fibonacci Sequence or not
	"""

	# n is a Fibonacci number only if fib_check1 or fib_check2 equates to a perfect square
	fib_check1 = 5 * n ** 2 + 4
	fib_check2 = 5 * n ** 2 - 4
	return fib_check1 % math.sqrt(fib_check1) == 0 or fib_check2 % math.sqrt(fib_check2) == 0


while True:
	# Presents the user with the possible choices
	menu_choice = menu()
	# If 1, generate a Fibonacci Sequence
	if menu_choice == 1:
		user_num = user_number()
		fib_seq = fibonacci_sequence(user_num)
		print("\nFibonacci Sequence:")
		print(fib_seq)
	# If 2, display a Fibonacci number at a given position
	elif menu_choice == 2:
		user_num = user_number()
		fib_num = fibonacci_number(user_num)
		print(f"\n{fib_num} is the number you are looking for.")
	# If 3, check if a number is part of the Fibonacci Sequence
	elif menu_choice == 3:
		user_num = user_number()
		check_num = is_number_fibonacci(user_num)
		if check_num:
			print(f"\n{user_num} is a Fibonacci number.")
		else:
			print(f"\n{user_num} is not a Fibonacci number.")
	# If 4, break the loop
	else:
		break
