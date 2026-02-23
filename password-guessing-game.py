import random 

easy_words = [ "apple","train","tiger","money","lion","india"]
medium_words = ["python","bottle","monkey","planet","laptop"]
hard_words = ["elephant","diamind","umbrella","computer","mountain"]

print("Welcom to the password guessing game")
print("Choose a difficulty level: easy, medium, hard")

level = input('Enter Difficulty:').lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words) 
else:
    print("Invalid choice. Default to easy level")
    secret = random.choice(easy_words)         

attempts = 0
print("\nGuess the secret Password")

while True:
    guess = input("Enter your guess:").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulation! You guessed it in{attempts} attempts.')
        break

    hint = ""

for i in range(len(secret)):
    if i < len(guess) and guess[i] == secret[i]:
        hint += guess[i]
    else:
        hint += "_"

    print("Hint", hint)
print("Game Over")
