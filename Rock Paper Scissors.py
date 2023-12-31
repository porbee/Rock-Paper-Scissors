'''

Rock Paper Scissors game

Rock > Scissors
Rock < Paper
Rock = Rock

Paper > Rock
Paper < Scissors
Paper = Paper

Scissors > Paper
Scissors < Rock
Scissors = Scissors

'''

choose_machine_mode_query = 'Which difficulty mode do you want to select?  '
print('      ____________________________________________________________________________________      ')
print('     |                                                                                    |     ')
print('     |    1) Impossible Mode             2) Normal Mode             3) Prediction Mode    |     ')
print('     |                                                                                    |     ')
print('      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾          ')
print()
choose_machine_mode_answer = input(choose_machine_mode_query)
print()
print()


# 100% win rate

def scissors():
    print()
    print()
    print('Scissors!!!')

def paper():
    print()
    print()
    print('Paper!!!')

def rock():
    print()
    print()
    print('Rock!!!')

if choose_machine_mode_answer == '1':
    three_optioned_query = 'Which one do you show? Rock, paper or scissors?  '
    print()
    three_optioned_answer = input(three_optioned_query)
    if three_optioned_answer == 'paper':
        scissors()
    elif three_optioned_answer == 'Paper':
        scissors()
    elif three_optioned_answer == 'PAPER':
        scissors()
    elif three_optioned_answer == 'pAPER':
        scissors()
    elif three_optioned_answer == 'rock':
        paper()
    elif three_optioned_answer == 'Rock':
        paper()
    elif three_optioned_answer == 'ROCK':
        paper()
    elif three_optioned_answer == 'rOCK':
        paper()
    elif three_optioned_answer == 'scissors':
        rock()
    elif three_optioned_answer == 'Scissors':
        rock()
    elif three_optioned_answer == 'SCISSORS':
        rock()
    elif three_optioned_answer == 'sCISSORS':
        rock()
    print()
    print()
    print('You lost, I won!')
    print()
    print()

# Normal mode
import numpy as np
import time

def draw():
    print()
    print()
    print('It is a draw. Want to play one more?')

def win():
    print()
    print()
    print('I won and you lost. Want another try?')

def lose():
    print()
    print()
    print('I lost and you won. Do you want to try once again?')

def response_delay():
    delay = 0.65
    time.sleep(delay)
    print('    Rock')
    print()
    print()
    print()
    time.sleep(delay)
    print('    Paper')
    print()
    print()
    print()
    time.sleep(delay)
    print('    Scissors!')
    print()
    print()
    print()
    time.sleep(0.91)

if choose_machine_mode_answer == '2':
    three_optioned_query_2 = 'Which one do you show? Rock (1), paper (2) or scissors (3)?  '
    three_optioned_answer_2 = input(three_optioned_query_2)
    machine_elected = np.random.choice([0,1,2], p = [(1/3), (1/3), (1/3)])
    print()
    print()
    print()
    response_delay()
    if machine_elected == 0:
        true_machine_elected = 'Rock'
        print('I elected ======> ' + true_machine_elected)
        print()
    elif machine_elected == 1:
        true_machine_elected = 'Paper'
        print('I elected ======> ' + true_machine_elected)
        print()
    elif machine_elected == 2:
        true_machine_elected = 'Scissors'
        print('I elected ======> ' + true_machine_elected)
        print()
    if three_optioned_answer_2 == '1':
        true_user_elected_answer = 'Rock'
        print('You elected ====> ' + true_user_elected_answer)
        print()
    elif three_optioned_answer_2 == '2':
        true_user_elected_answer = 'Paper'
        print('You elected ====> ' + true_user_elected_answer)
        print()
    elif three_optioned_answer_2 == '3':
        true_user_elected_answer = 'Scissors'
        print('You elected ====> ' + true_user_elected_answer)
        print()
    if true_machine_elected == true_user_elected_answer:
        draw()
    elif true_machine_elected == 'Rock' and true_user_elected_answer == 'Paper':
        lose()
    elif true_machine_elected == 'Rock' and true_user_elected_answer == 'Scissors':
        win()
    elif true_machine_elected == 'Paper' and true_user_elected_answer == 'Rock':
        win()
    elif true_machine_elected == 'Paper' and true_user_elected_answer == 'Scissors':
        lose()
    elif true_machine_elected == 'Scissors' and true_user_elected_answer == 'Paper':
        win()
    elif true_machine_elected == 'Scissors' and true_user_elected_answer == 'Rock':
        lose()

# The machine can learn!
import math

# Making 'Historial' dictionary to record result of matches
historial = []

# Making the historical data of users actions
player_actions = []

# Making the probability of any result from the machine change depending on what the user usually chooses
# For example; if the user plays 'paper' a lot, the machine will play a lot of 'scissors'
machine_election_probability = [1/3,1/3,1/3]

# Show historical record of match results
def historical_match_results():
    list_size = len(historial)
    player_victory_quantity = historial.count(' Machine Defeat')
    player_defeat_quantity = historial.count('Machine Victory')
    draw_quantity = historial.count('      Draw     ')
    win_rate_percentage = int((player_victory_quantity/list_size)*100)
    win_rate_percentage_size = len(str(win_rate_percentage))
    print('      _______________________________________________________________________________      ')
    print('     |                                                                               |     ')
    print(f'     |     Historical Record of Match Results             Matches played ====> {list_size}     |     ')
    print('     |                                                                               |     ')
    print('     |                                                                               |     ')
    if list_size == 1:
        print(f'     |       1st match                                         {historial[0]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
    elif list_size == 2:
        print(f'     |       1st match                                         {historial[0]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
        print(f'     |       2nd match                                         {historial[1]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
    elif list_size == 3:
        print(f'     |       1st match                                         {historial[0]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
        print(f'     |       2nd match                                         {historial[1]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
        print(f'     |       3rd match                                         {historial[2]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
    elif list_size >= 4:
        print(f'     |       1st match                                         {historial[0]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
        print(f'     |       2nd match                                         {historial[1]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
        print(f'     |       3rd match                                         {historial[2]}       |     ')
        print('     |                                                                               |     ')
        print('     |                                                                               |     ')
        for number in range(4, list_size):
            print(f'     |       {number}th match                                         {historial[number-1]}       |     ')
            print('     |                                                                               |     ')
            print('     |                                                                               |     ')
            if number == (list_size-1):
                print(f'     |       {list_size}th match                                         {historial[-1]}       |     ')
                print('     |                                                                               |     ')
                print('     |                                                                               |     ')
    print(f'     |        Total draws = {draw_quantity}      Total victories = {player_victory_quantity}      Total defeats = {player_defeat_quantity}        |     ')
    print('     |                                                                               |     ')
    print('     |                                                                               |     ')
    if win_rate_percentage_size == 1:
        print(f'     |                           Your total Win Rate = {win_rate_percentage}%                            |     ')
    elif win_rate_percentage_size == 2:
        print(f'     |                           Your total Win Rate = {win_rate_percentage}%                           |     ')
    elif win_rate_percentage_size == 3:
        print(f'     |                           Your total Win Rate = {win_rate_percentage}%                          |     ')
    print('     |                                                                               |     ')
    print('     |                                                                               |     ')
    print('      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾     ')

# Make other functions for when the player wants to play another game
def draw2():
    historial.append('      Draw     ')
    print()
    print()
    rematch = input('It is a draw. Want to play one more? Y/N  ')
    print()
    print()
    if rematch == 'Y':
        repeatMode()
    elif rematch == 'N':
        show_historical_record = input('Do you prefer to see your historical record? Y/N  ')
        if show_historical_record == 'Y':
            historical_match_results()
        elif show_historical_record == 'N':
            pass
    else:
        pass

def win2():
    historial.append('Machine Victory')
    print()
    print()
    rematch = input('I won and you lost. Want another try? Y/N  ')
    print()
    print()
    if rematch == 'Y':
        repeatMode()
    elif rematch == 'N':
        show_historical_record = input('Do you prefer to see your historical record? Y/N  ')
        if show_historical_record == 'Y':
            historical_match_results()
        elif show_historical_record == 'N':
            pass
    else:
        pass

def lose2():
    historial.append(' Machine Defeat')
    print()
    print()
    rematch = input('I lost and you won. Do you want to try once again? Y/N  ')
    print()
    print()
    if rematch == 'Y':
        repeatMode()
    elif rematch == 'N':
        show_historical_record = input('Do you prefer to see your historical record? Y/N  ')
        if show_historical_record == 'Y':
            historical_match_results()
        elif show_historical_record == 'N':
            pass
    else:
        pass

# Looping the code if try again prompt == yes
def repeatMode():
    three_optioned_query_3 = 'Which one do you show? Rock (1), paper (2) or scissors (3)?  '
    three_optioned_answer_3 = input(three_optioned_query_3)
    if three_optioned_answer_3 == '1':
        player_actions.append('Rock')
    elif three_optioned_answer_3 == '2':
        player_actions.append('Paper')
    elif three_optioned_answer_3 == '3':
        player_actions.append('Scissors')
    else:
        pass
    machine_elected = np.random.choice([0,1,2], p = machine_election_probability)
    print()
    print()
    print()
    response_delay()
    if machine_elected == 0:
        true_machine_elected = 'Rock'
        print('I elected ===========> ' + true_machine_elected)
        print()
    elif machine_elected == 1:
        true_machine_elected = 'Paper'
        print('I elected ===========> ' + true_machine_elected)
        print()
    elif machine_elected == 2:
        true_machine_elected = 'Scissors'
        print('I elected ===========> ' + true_machine_elected)
        print()
    if three_optioned_answer_3 == '1':
        true_user_elected_answer = 'Rock'
        print('You elected =========> ' + true_user_elected_answer)
        print()
    elif three_optioned_answer_3 == '2':
        true_user_elected_answer = 'Paper'
        print('You elected =========> ' + true_user_elected_answer)
        print()
    elif three_optioned_answer_3 == '3':
        true_user_elected_answer = 'Scissors'
        print('You elected =========> ' + true_user_elected_answer)
        print()
    else:
        print("The number I am trying to accept from you doesn't figure between the options")
        print()
    if true_machine_elected == true_user_elected_answer:
        draw2()
    elif true_machine_elected == 'Rock' and true_user_elected_answer == 'Paper':
        lose2()
    elif true_machine_elected == 'Rock' and true_user_elected_answer == 'Scissors':
        win2()
    elif true_machine_elected == 'Paper' and true_user_elected_answer == 'Rock':
        win2()
    elif true_machine_elected == 'Paper' and true_user_elected_answer == 'Scissors':
        lose2()
    elif true_machine_elected == 'Scissors' and true_user_elected_answer == 'Paper':
        win2()
    elif true_machine_elected == 'Scissors' and true_user_elected_answer == 'Rock':
        lose2()
    level_rock = player_actions.count('Rock')
    level_paper = player_actions.count('Paper')
    level_scissors = player_actions.count('Scissors')
    rock_modifier_not_processed = ((0.25*math.e)**(-0.25*level_rock))-1
    if rock_modifier_not_processed > 1:
        rock_modifier = 1
    else: rock_modifier = rock_modifier_not_processed
    paper_modifier_not_processed = ((0.25*math.e)**(-0.25*level_paper))-1
    if paper_modifier_not_processed > 1:
        paper_modifier = 1
    else: paper_modifier = paper_modifier_not_processed
    scissors_modifier_not_processed = ((0.25*math.e)**(-0.25*level_scissors))-1
    if scissors_modifier_not_processed > 1:
        scissors_modifier = 1
    else: scissors_modifier = scissors_modifier_not_processed
    rock_probability_change = 1+(scissors_modifier-paper_modifier)
    paper_probability_change = 1+(rock_modifier-scissors_modifier)
    scissors_probability_change = 1+(paper_modifier-rock_modifier)
    machine_election_probability[0] = machine_election_probability[0]*rock_probability_change
    if machine_election_probability[0] > (2/3):
        machine_election_probability[0] = (2/3)
    machine_election_probability[1] = machine_election_probability[1]*paper_probability_change
    if machine_election_probability[1] > (2/3):
        machine_election_probability[1] = (2/3)
    machine_election_probability[2] = machine_election_probability[2]*scissors_probability_change
    if machine_election_probability[2] > (2/3):
        machine_election_probability[2] = (2/3)

# Tweaking the normal mode so it can be suited to the new functions
if choose_machine_mode_answer == '3':
    three_optioned_query_3 = 'Which one do you show? Rock (1), paper (2) or scissors (3)?  '
    three_optioned_answer_3 = input(three_optioned_query_3)
    if three_optioned_answer_3 == '1':
        player_actions.append('Rock')
    elif three_optioned_answer_3 == '2':
        player_actions.append('Paper')
    elif three_optioned_answer_3 == '3':
        player_actions.append('Scissors')
    else:
        pass
    machine_elected = np.random.choice([0,1,2], p = machine_election_probability)
    print()
    print()
    print()
    response_delay()
    if machine_elected == 0:
        true_machine_elected = 'Rock'
        print('I elected ===========> ' + true_machine_elected)
        print()
    elif machine_elected == 1:
        true_machine_elected = 'Paper'
        print('I elected ===========> ' + true_machine_elected)
        print()
    elif machine_elected == 2:
        true_machine_elected = 'Scissors'
        print('I elected ===========> ' + true_machine_elected)
        print()
    if three_optioned_answer_3 == '1':
        true_user_elected_answer = 'Rock'
        print('You elected =========> ' + true_user_elected_answer)
        print()
    elif three_optioned_answer_3 == '2':
        true_user_elected_answer = 'Paper'
        print('You elected =========> ' + true_user_elected_answer)
        print()
    elif three_optioned_answer_3 == '3':
        true_user_elected_answer = 'Scissors'
        print('You elected =========> ' + true_user_elected_answer)
        print()
    else:
        print("The number I am trying to accept from you doesn't figure between the options")
        print()
    if true_machine_elected == true_user_elected_answer:
        draw2()
    elif true_machine_elected == 'Rock' and true_user_elected_answer == 'Paper':
        lose2()
    elif true_machine_elected == 'Rock' and true_user_elected_answer == 'Scissors':
        win2()
    elif true_machine_elected == 'Paper' and true_user_elected_answer == 'Rock':
        win2()
    elif true_machine_elected == 'Paper' and true_user_elected_answer == 'Scissors':
        lose2()
    elif true_machine_elected == 'Scissors' and true_user_elected_answer == 'Paper':
        win2()
    elif true_machine_elected == 'Scissors' and true_user_elected_answer == 'Rock':
        lose2()
    level_rock = player_actions.count('Rock')
    level_paper = player_actions.count('Paper')
    level_scissors = player_actions.count('Scissors')
    rock_modifier_not_processed = ((0.25*math.e)**(-0.25*level_rock))-1
    if rock_modifier_not_processed > 1:
        rock_modifier = 1
    else: rock_modifier = rock_modifier_not_processed
    paper_modifier_not_processed = ((0.25*math.e)**(-0.25*level_paper))-1
    if paper_modifier_not_processed > 1:
        paper_modifier = 1
    else: paper_modifier = paper_modifier_not_processed
    scissors_modifier_not_processed = ((0.25*math.e)**(-0.25*level_scissors))-1
    if scissors_modifier_not_processed > 1:
        scissors_modifier = 1
    else: scissors_modifier = scissors_modifier_not_processed
    rock_probability_change = 1+(scissors_modifier-paper_modifier)
    paper_probability_change = 1+(rock_modifier-scissors_modifier)
    scissors_probability_change = 1+(paper_modifier-rock_modifier)
    machine_election_probability[0] = machine_election_probability[0]*rock_probability_change
    if machine_election_probability[0] > (2/3):
        machine_election_probability[0] = (2/3)
    machine_election_probability[1] = machine_election_probability[1]*paper_probability_change
    if machine_election_probability[1] > (2/3):
        machine_election_probability[1] = (2/3)
    machine_election_probability[2] = machine_election_probability[2]*scissors_probability_change
    if machine_election_probability[2] > (2/3):
        machine_election_probability[2] = (2/3)