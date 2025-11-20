import random
import time
import sys

from draw import draw_d20, draw_d6, draw_d4

def check_player_alive(lives: int) -> None:
    if lives <= 0:
        print('You died!')
        sys.exit()

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    print_dramatic_text('Welcome to Josies trivia game!!')

    lives = 5
    answer = input('Question 1: What is the slowest animal on the Earth?\n')
    if answer.lower() == 'slug':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)

    answer = input('Question 2: What is the fastest animal on earth?\n')
    if answer.lower() == 'hawk':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)

    answer = input('Question 3:What is the prettiest animal that can fly?\n')
    if answer.lower() == 'butterfly':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)

    questions = [
        'Question 4: Do you like food?',
        'Question 4: Would you ever want to be a zombie?',
        'Question 4: Do you sing in the shower?'
    ]
 
    answers = [
        'yes',
        'yes',
        'yes' 
    ]

    r = random.randint(0, 2)
    answer = input(questions[r] + ' ')
    if answer.lower() == answers[r]:
        print_dramatic_text('correct!')
    else:
        print_dramatic_text('incorrect ...')
        lives -= 1
        check_player_alive(lives)

    # add more questions?

    print_dramatic_text('Congrats you finished the game !! :( ')
 
    

          
      





