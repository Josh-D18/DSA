# Function 1:
# Name: wins_rock_scissors_paper
# Parameters: 2 strings
# Return: a boolean value
# Description: This function is passed two strings. Each of the two strings is going to be one of 3 values:
# rock
# paper
# scissors
# The strings may have any casing. Rock, ROCK, roCK are all possible and valid.
# The first string represents what the player threw in a game of rocks paper scissors. The second string
# represents what the opponent threw. This function returns true, if the player won, and false if it was a tie
# or a loss.
# In a game of rock, paper, scissors, each player "throws" one of the 3 items. The winner is determined by
# the following rules
# rock beats scissors
# paper beats rock
# scissor beats paper




def wins_rock_scissors_paper(string, string2):
    player_options = ["rock", "paper", "scissors"]
    player_selection = string.lower()
    computer_selection = string2.lower()

    if player_selection in player_options and computer_selection in player_options:
        
        if player_selection == computer_selection:
            return False
        elif player_selection == "rock" and computer_selection == "scissors":
            return True
        elif player_selection == "paper" and computer_selection == "rock":
            return True
        elif player_selection == "scissors" and computer_selection == "paper":
            return True
        else:
            return False
    else:
        return False  
    
print(wins_rock_scissors_paper("paper", "rock"))






# Function 2:
# Name: factorial
# Parameters: a number (int)
# Return: a number (int)
# Description: This function is passed a non-negative integer, that we will call n in this description. the
# function returns n! (pronounced n factorial). n! = n * (n-1) * (n-2)... * 1 Thus, 3! = 3 * 2 * 1. Note that 0! is 1
# by definition.

def factorial(n):
    if n <= 1:
        return n
    
    return n * factorial(n - 1)

print(factorial(7))


# Function 3:
# Name: Fibonacci
# Parameters: a number (int)
# Return: a number (int)
# Description: This function is passed a non-negative integer, that we will call n in this description. the
# function returns the nth Fibonacci number in the Fibonacci sequence.
# The nth Fibonacci number is the sum of the 2 previous Fibonacci numbers. Here is a sample of the
# Fibonacci series
# 1, 1, 2, 3, 5, 8, 13, 21, ..
# This means that your function should return 13 if the parameter sent to it is 7 and 1 if the parameter is 2


def fibonacci(n):
    if n <= 1:
        return n
    return  fibonacci(n - 1) +  fibonacci(n - 2)

print(fibonacci(7))