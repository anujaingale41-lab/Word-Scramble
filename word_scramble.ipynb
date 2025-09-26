import random
import time

WORDS = {
    "easy": ["cat", "dog", "sun", "pen", "cup"],
    "medium": ["python", "object", "string", "syntax", "loop"],
    "hard": ["developer", "functionality", "inheritance", "dictionary", "encapsulation"]
}

TIME_LIMITS = {
    "easy": 60,
    "medium": 30,
    "hard": 15
}

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy\n2. Medium\n3. Hard")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        return "easy"
    elif choice == "2":
        return "medium"
    elif choice == "3":
        return "hard"
    else:
        print("Invalid choice. Defaulting to Easy.")
        return "easy"

def play_game():
    score = 0
    print("🧩 Welcome to Word Scramble!")

    difficulty = choose_difficulty()
    time_limit = TIME_LIMITS[difficulty]
    word_list = WORDS[difficulty]

    print(f"\nYou chose '{difficulty.capitalize()}' difficulty.")
    print(f"You have {time_limit} seconds to unscramble each word.\n")

    while True:
        word = random.choice(word_list)
        scrambled = scramble_word(word)
        print(f"Scrambled word: {scrambled}")

        start_time = time.time()
        guess = input("Your guess: ")
        elapsed_time = time.time() - start_time

        if elapsed_time > time_limit:
            print("⏰ Time's up!")
        elif guess.lower() == word:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct word was: {word}")

        print(f"Your current score: {score}")
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print(f"Final score: {score}. Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
