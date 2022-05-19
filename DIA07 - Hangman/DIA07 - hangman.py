import random
import hangman_ascii

words = ["ardvark", "baboon", "camel"]

word = random.choice(words)
guessed_word = []
for _ in word: # for _ in range(len(chosen_word)):
    guessed_word.append("_") # display += "_"
guessed_word_str = ' '.join(map(str, guessed_word))
#print(guessed_word_str)

guessed_letters_list = [] 
end_of_game = False
lives = 7
while end_of_game == False:
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in guessed_letters_list:
        print(f"You have already said letter {guessed_letter}")
    else:
        guessed_letters_list.append(guessed_letter)
        if guessed_letter not in word:
            lives -= 1
            if lives == 0:
                print("Wrong letter. No lives remaining. You lose.")
                end_of_game == True
            else:
                print(f"You guessed {guessed_letter}. It's not in the word. You lose a life. Remaining lives = {lives}")
        elif "_" not in guessed_word:
            end_of_game = True
            print("You win")
        else:
            for i in range(len(word)):
                if word[i] == guessed_letter:
                    guessed_word[i] = guessed_letter
            guessed_word_str = ' '.join(map(str, guessed_word))
    print(guessed_word_str)
    print(hangman_ascii.hangman[6 - lives])


    

