from tkinter import *
from tkinter import messagebox
import words

root = Tk()
word = words.getword()

root.geometry("500x500")
root.title("Word Guesser")

green = "#17b505"
yellow = "#f5e50c"
black = "#000000"
white = "#ffffff"

root.config(bg=black)

guessNum = 1

wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

def getGuess():
    
    global word
    guess = wordInput.get()
    
    global guessNum
    guessNum += 1
    
    if guessNum < 6:
        
        if len(guess) == 5:
            #correct guess
            if word == guess: 
                messagebox.showinfo("correct!", f"correct! The word was {word.title()}")
            #incorrect guess
            else:
                for i, letter in enumerate(guess):
                    
                    label = Label(root, text=letter.upper())
                    label.grid(row=guessNum, column=i, padx=10, pady=10)
                    
                    #guess the letter correct
                    if letter == word[i]:
                        label.config(bg=green, fg=black)
                        
                    #correct letter but wrong position
                    if letter in word and not letter == word[i]:
                        label.config(bg=yellow, fg=black)
                        
                    #letter not in word
                    if letter not in word:
                        label.config(bg=black, fg=white)

        else:
            messagebox.showerror("please use 5 characters", "please use 5 characters in your guess")

    else:
        messagebox.showerror("You Lose!", f"You Lose! The word was {word}")



wordGuessButton = Button(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2)



root.mainloop()