
import random

def main():
	number = random.randint(1, 25)
	attempts = 3
	print("Guess the number between 1 and 25. You have 3 attempts.")
	for attempt in range(1, attempts + 1):
		while True:
			guess = input(f"Attempt {attempt}: Enter your guess: ")
			if not guess.isdigit():
				print("Invalid input. Please enter a number.")
				continue
			guess = int(guess)
			if guess < 1 or guess > 25:
				print("Number must be between 1 and 25.")
				continue
			break
		if guess == number:
			print("Congratulations! You guessed the correct number.")
			return
		else:
			if guess < number:
				print("Hint: The number is higher.")
			else:
				print("Hint: The number is lower.")
	print(f"Sorry, you've used all attempts. The number was {number}.")

if __name__ == "__main__":
	main()
