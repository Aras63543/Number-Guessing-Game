import random # Import the random module to generate random numbers

print("Welcome to the Number Guessing Game! Guess a number 1-100.") 
print("Select difficulty:\n1. Easy (5 tries)\n2. Medium (3 tries)\n3. Hard (1 tries)")

difficulty = int(input("Please enter a number (1-3): ")) 

if difficulty == 1:
    chances = 5
elif difficulty == 2:
    chances = 3               
elif difficulty == 3:
    chances = 2
else:
    chances = int(input("ERROR! Please enter a number 1-3: "))

print(f"You have {chances} chances. Good luck!") # Display the number of attempts the player has


answer = random.randint(1,100) # Generate a random number between 1 and 100 and store it in 'answer'

for attempt in range(1, chances + 1):
    guess = int(input(f'Attempt {attempt}/{chances} Chances - Enter your guess:')) # Loop for each attempt and ask the player for a guess

    if guess > answer:
        print("Too high!")

    elif guess < answer:
        print("Too Low!")

    else: 
        print(f"Congrats! You guessed it in {attempt} ")
        break
else: 
    print(f"No, The number was {answer}")



