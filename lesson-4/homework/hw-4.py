##Questions

##1.Loops quiz (12.5 out of 13)
##2.continue → Skips the rest of the current loop iteration and moves to the next one.
     ##break → Immediately exits the loop entirely.
##3. for loop: Used when the number of iterations is known or finite (e.g., looping over a list or range).
##while loop: Used when the number of iterations is unknown and depends on a condition being True.
##4.Used to iterate over multi-level data (e.g., rows and columns).
##example:

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
##This prints all combinations of i and j.


##Homeworks

##num1

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    diff1 = c1 - c2
    diff2 = c2 - c1
    
    result = list(diff1.elements()) + list(diff2.elements())
    return result
print(uncommon_elements([1, 1, 2], [2, 3, 4])) 
print(uncommon_elements([1, 2, 3], [4, 5, 6])) 
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  


##num2

def print_squares_less_than(n):
    for i in range(1, n):
        print(i * i)
print_squares_less_than(5)


##num3

def insert_underscores(txt):
    result = []
    i = 0
    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0 and i != len(txt) - 1:
            if txt[i] in 'aeiou' or (i > 0 and result[-2] == '_'):
                if i + 1 < len(txt) - 1:
                    result.append(txt[i + 1])
                    result.append('_')
                    i += 1
                else:
                    result.append(txt[i + 1])
                    i += 1
            else:
                result.append('_')
        i += 1
    return ''.join(result)
print(insert_underscores("hello"))
print(insert_underscores("assalom")) 
print(insert_underscores("abcabcdabcdeabcdefabcdefg"))  


##numm4

import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"Guess a number (Attempts left: {attempts}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("You guessed it right!")
            return

        attempts -= 1

    print("You lost. Want to play again?")

def main():
    while True:
        play_game()
        retry = input("Play again? (Y/YES/y/yes/ok): ").strip().lower()
        if retry not in ['y', 'yes', 'ok']:
            print("Thanks for playing!")
            break

main()


#num5

def check_password():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password is too short.")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")

check_password()


##num6

for num in range(2, 101): 
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


##Bonus Challage

import random

def get_winner(player, computer):
    if player == computer:
        return 'draw'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'player'
    else:
        return 'computer'

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins the match.")
    
    while player_score < 5 and computer_score < 5:
        player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if player_choice not in options:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)

        if winner == 'player':
            player_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score => You: {player_score} | Computer: {computer_score}")
        print("-" * 30)

    if player_score == 5:
        print(" You won the match!")
    else:
        print(" Computer won the match!")

play_game()
