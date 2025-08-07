import random

while True:
    cpu = random.randint(1, 100)

    difficulty = input("Choose level (easy = 15 tries / hard = 10 tries): ").lower()
    if difficulty == "easy":
        attempts = 15
    elif difficulty == "hard":
        attempts = 10
    else:
        print("Invalid Level!")
        continue

    while attempts > 0:
        user = int(input("Guess the number from (1-100): "))

        if user == cpu:
            print("🎉 Correct guess! You win!")
            break
        elif user > cpu:
            print("📉 Too high! Try a lower number.")
        elif user < cpu:
            print("📈 Too low! Try a higher number.")

        attempts -= 1
        print(f"🔁 Attempts left: {attempts}\n")

    # After guessing loop
    if attempts == 0 and user != cpu:
        print(f"😢 Out of tries! You lose! The correct number was {cpu}")

    user_newmatch = input("Do you want to play again? (yes/no): ").lower()
    if user_newmatch == "no":
        print("👋 Thanks for playing!")
        exit()
    elif user_newmatch == "yes":
        continue  # restarts the game
    else:
        print("⚠️ Please type 'yes' or 'no'")
