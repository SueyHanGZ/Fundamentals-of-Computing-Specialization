# -*- coding: utf-8 -*-

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number 
    secret_number = random.randrange(0,100)
    global count
    count = 7
    # remove this when you add your code    
    return range100()
        

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number 
    secret_number = random.randrange(0,100) 
    global count
    count = 7
    print ('New game. Range is from 0 to 100.')
    print ('Number of remaining guesses is 7.')
    print
    return


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number 
    secret_number = random.randrange(0,1000)
    global count
    count = 10
    print ('New game. Range is from 0 to 1000.')
    print ('Number of remaining guesses is 10.')
    print
    return

    
def input_guess(guess):
    # main game logic goes here	
    print ('Guess was ' + guess)
    # print (secret_number)
    global count    
    count -= 1
    if count >= 0:        
        guess = int(guess)
        if guess == secret_number:
            print ('Correct!')
            print 
            return new_game()
        elif guess > secret_number:
            print ('Number of remaining guesses is ' + str(count))
            print ('Lower!')        
        else:
            print ('Number of remaining guesses is ' + str(count))
            print ('Higher!')
        print
    
    if count == 0:
        print ('Number of remaining guesses is 0')
        print ('You ran out of guesses. The number was ' + str(secret_number))
        print 
        return new_game()
    

    
# create frame
f = simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements and start frame
f.add_button('Range is [0, 100)', range100, 200)
f.add_button('Range is [0, 1000)', range1000, 200)
f.add_input('Enter a guess', input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
