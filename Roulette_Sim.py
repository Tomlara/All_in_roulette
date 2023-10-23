# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:44:26 2023

@author: vr198
"""

import random
import matplotlib.pyplot as plt 
import numpy

bankroll = int(input("What is your starting balance (in whole $$): "))
Track_Profit = [bankroll]
simulation = input("Would you like to simulate this bet (Y/N):")



def spins():
    global pockets
    pockets = {'00': 'green', '0': 'green', '1': 'red', '2': 'black',
             '3': 'red', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
             '8': 'black', '9': 'red', '10': 'black', '11': 'red',
             '12': 'black', '13': 'red', '14': 'black', '15': 'red',
             '16': 'black', '17': 'red', '18': 'black', '19': 'red',
             '20': 'black', '21': 'red', '22': 'black', '23': 'red',
             '24': 'black', '25': 'red', '26': 'black', '27': 'red',
             '28': 'black', '29': 'red', '30': 'black', '31': 'red',
             '32': 'black', '33': 'red', '34': 'black', '35': 'red',
             '36': 'black'}

    result = random.choice(list(pockets.keys()))
    return result


def bet_value(bet_type):
    if bet_type == 1:
        bet_val = int(input("Is it an EVEN (1) or an ODD (2) bet?: "))
        return bet_val
    if bet_type == 2:
        bet_val = int(input("Is it a RED (1) or a BLACK (2) bet?: "))
        return bet_val
    if bet_type == 8:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        return bet_list
    if bet_type == 9:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        num3 = int(input("What is your third number?: "))
        bet_list.append(num3)
        return bet_list
    if bet_type == 10:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        num3 = int(input("What is your third number?: "))
        bet_list.append(num3)
        num4 = int(input("What is your fourth number?: "))
        bet_list.append(num4)
        return bet_list
    if bet_type == 11:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        num3 = int(input("What is your third number?: "))
        bet_list.append(num3)
        num4 = int(input("What is your fourth number?: "))
        bet_list.append(num4)
        num5 = int(input("What is your fifth number?: "))
        bet_list.append(num5)
        num6 = int(input("What is your sixth number?: "))
        bet_list.append(num6)
        return bet_list
    if bet_type == 12:
        bet_list = ['00', '0', '1', '2', '3']
        return bet_list
    if bet_type == 13:
        bet_val = input("What number do you want to choose 00, 0, 1-36?: ")
        return bet_val


def adjusted_bankroll(result, balance, bet_type, bet_val, bet):
    balance -= bet
    # Adjust player balance for even/odd bets.
    if (bet_type == 1) and (bet_val == 1):  # Even
        if (int(result) % 2 == 0) and (int(result) != 0):
            payout = bet
            balance += bet + payout
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    
    if (bet_type == 1) and (bet_val == 2):  # Odd
        if int(result) % 2 == 1:
            payout = bet
            balance += bet + payout
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust player balance for red/black bets.
    if (bet_type == 2) and (bet_val == 1):  # Red
        if pockets[result] == 'red':
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if (bet_type == 2) and (bet_val == 2):  # Black
        if pockets[result] == 'black':
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust player balance for the set of twelves.k
    if bet_type == 3:  # First Twelve
        if (int(result) >= 1) and (int(result) <= 12):
            balance += 3 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 4:  # Second Twelve
        if (int(result) >= 13) and (int(result) <= 24):
            balance += 3 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 5:  # Third Twelve
        if (int(result) >= 25) and (int(result) <= 36):
            balance += 3 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust the player balance for the first and second set of eighteen.
    if bet_type == 6:  # First Eighteen
        if (int(result) >= 1) and (int(result) <= 18):
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 7:  # Second Eighteen
        if (int(result) >= 19) and (int(result) <= 36):
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust for betting multiple numbers at the same time.
    if bet_type == 8:  # Combination of two numbers
        if int(result) in bet_val:
            balance += 18 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 9:  # Combination of three numbers
        if int(result) in bet_val:
            balance += 12 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 10:  # Combination of four numbers
        if int(result) in bet_val:
            balance += 9 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 11:  # Combination of six numbers
        if int(result) in bet_val:
            balance += 6 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 12:  # Combination of 00-0-1-2-3
        if result in bet_val:
            balance += 7 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust player balance if bet a single number.
    if bet_type == 13:
        if result == bet_val:
            payout = 36 * bet
            balance += payout
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance

    global bankroll 
    bankroll = balance
    Track_Profit.append(balance)

    return (prompt, bankroll,Track_Profit)

def Add_Bet_to_system(System):
    
    bet_type = int(input("What type of bet? Choose one of the given numbers:\n"
                         "1 = Even/Odd\n"
                         "2 = Red/Black\n"
                         "3 = First Twelve (1-12)\n"
                         "4 = Second Twelve (13-24)\n"
                         "5 = Third Twelve (25-36)\n"
                         "6 = First Eighteen (1-18)\n"
                         "7 = Second Eighteen (19-36)\n"
                         "8 = Combination of Two Numbers\n"
                         "9 = Combination of Three Numbers\n"
                         "10 = Combination of Four Numbers\n"
                         "11 = Combination of Six Numbers\n"
                         "12 = Combination of 1-2-3-0-00\n"
                         "13 = One Number (Straight Up)"))
    bet = int(input("How much do you want to bet each simuation for this bet choice?: "))
    choice = bet_value(bet_type) 
    System.append([bet_type,choice,bet])
    keep_adding = input("Would you like to add to the ?: ")
    return keep_adding,System


keep_playing = 'yes'
keep_adding = 'yes'


if (simulation.lower() == 'yes') or (simulation.lower() == 'y'):
    
    num_sims = int(input("Please enter how many times you would like to simulate:"))
    System = []
    while (keep_adding.lower() == 'yes') or (keep_adding.lower() == 'y'):
        keep_adding,System = Add_Bet_to_system(System)
    
    print(System)
    print(range(len(System)))
    
    
    for i in range(num_sims):
        Outcome = spins()
        for j in range(len(System)):
            (prmpt,balance,Track_Profit) = adjusted_bankroll(Outcome, bankroll, System[j][0], System[j][1], System[j][2])
            print("\nThe winning number is: %s!" % Outcome)
            print(prmpt)
            print("This is your tracked balance",Track_Profit)
    
    Track_Profit = Track_Profit[0::len(System)]
    print("This is tracked profit",Track_Profit)
    
    x = range(num_sims+1)
    ar = numpy.array(x)
    x =  ar + 1

    print(x)
    plt.plot(x,Track_Profit) 
    plt.ylabel("Balance")
    plt.xlabel("Spins") 
    plt.title("Roulette Simulation")  
    plt.show() 
    
    
        
    
else:
    
    while (keep_playing.lower() == 'yes') or (keep_playing.lower() == 'y'):
        #bet = int(input("How much do you want to bet each simuation for this bet choice?: "))
        bet_type = int(input("What type of bet? Choose one of the given numbers:\n"
                             "1 = Even/Odd\n"
                             "2 = Red/Black\n"
                             "3 = First Twelve (1-12)\n"
                             "4 = Second Twelve (13-24)\n"
                             "5 = Third Twelve (25-36)\n"
                             "6 = First Eighteen (1-18)\n"
                             "7 = Second Eighteen (19-36)\n"
                             "8 = Combination of Two Numbers\n"
                             "9 = Combination of Three Numbers\n"
                             "10 = Combination of Four Numbers\n"
                             "11 = Combination of Six Numbers\n"
                             "12 = Combination of 1-2-3-0-00\n"
                             "13 = One Number (Straight Up)"))
        #System = []
        #System.append(bet_type)
        bet = int(input("How much do you want to bet each simuation for this bet choice?: "))
        System = []
        System.append([bet_type,bet])
        print(System)
        
    (prmpt, balance,Track_Profit) = adjusted_bankroll(spins(), bankroll, bet_value(bet_type))
    print("\nThe winning number is: %s!" % spins())
    print(prmpt)
    print("This is your tracked balance",Track_Profit)
    bankroll = balance
    keep_playing = input("Would you like to keep playing? (Y/N): ")