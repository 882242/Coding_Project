print("Guess the 5 letter word!")

TheWord = ("Yeild") or ("yeild")
while True:
    GuessedWord = input("Enter your guess: ").strip()  # Remove leading/trailing whitespace

    if len(GuessedWord) != 5:  # Check if input is exactly 5 characters
        print("Invalid input! Please enter a word with exactly 5 letters.")
        continue
    elif not GuessedWord.isalpha():  # Check if input contains only letters
        print("Invalid input! Please enter alphabetic characters only.")
        continue
    elif GuessedWord == TheWord:
        print("Congratulations! You guessed the word!")
        break
    else:
        print("Incorrect! Try again.")
        continue

