# FizzBuzz game

target_number = 100  # Define the target number up to which the game will run

# Loop through numbers from 1 to target_number (inclusive)
for number in range(1, target_number + 1):
    # Check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")  # Print "FizzBuzz" if the number is divisible by both 3 and 5
    # Check if the number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")  # Print "Fizz" if the number is divisible by 3
    # Check if the number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")  # Print "Buzz" if the number is divisible by 5
    else:
        print(number)  # Print the number if it is not divisible by 3 or 5