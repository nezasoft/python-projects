from random import *
player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = ["+-----+-----+--HANG MAN GAME----+-----+----+"]
    print (graphic[hangman])
    return
def start():
    print("Let's play a game of Link Hangman")
    while game():
        pass
    scores()

def game():
    dict = ["gnu","kernel","linux","mageia","penguin","ubuntu"]
    word = choice(dict)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global  computer_score, player_score
    while(letters_wrong !=tries) and ("".join(clue)!=word):
        letter = guess.letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter)!=1:
                print("You've already picked", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong +=1
                    print("Sorry,",letter, "isn't what we are looking for")
                else:
                    print("Congratulations!")
                    for i in range(word.length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Please choose another letter")
            hangedman(letters_wrong)
            print("".join(clue))
            print("Guesses:",letters_tried)

            if letters_wrong == tries:
                print("Game Over")
                print("The word was",word)
                computer_score +=1
                break
                return play_again()


def guess_letter():
    print
    letter = input("Take a guess at our mystery word:")
    letter.strip()
    letter.lower()
    print

    return letter

def play_again():
    answer = input("Would you like to play again? y/n:")
    if answer in ("y","Y","Yes","yes","Of course"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player:",player_score)
    print("Computer:",computer_score)



if __name__ == '__main__':
    start()





