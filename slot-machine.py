import random

# symbols
symbols_list = ["Cherry", "Lemon", "Orange", "Plum", "Watermelon", "Bar", "Bell", "Seven", "Wild", "Scatter"]

#1 get deposit
def get_deposit():
    while True:
        deposit = input("plz enter deposit £")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("must be greater than 0. plz enter deposit")
        else:
            print("Invalid input. Please enter a numeric value.")

    return deposit

#2 get bet
def get_bet_amount(deposit):
    while True:
        bet_amount = input("plz enter bet amount £")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount > deposit:
                print("plz enter bet amount that is within your deposit amount")
            elif bet_amount <= 0:
                print("plz enter bet amount above 0")
            else:
                break
        else:
            print("Invalid input. Please enter a numeric value.")

    return bet_amount

#3 get no. of lines
def get_number_of_lines():
    while True:
        number_of_lines = input("Please enter the number of lines to bet on, between 1 - 3: ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if number_of_lines < 1 or number_of_lines > 3:
                print("Please enter a number of lines within the range of 1 - 3")
            else:
                break
        else:
            print("Invalid input. Please enter a valid numeric value.")

    return number_of_lines


#4 spin slot line 1
def spin_slot_line_1():
    spin_slot1 = random.choice(symbols_list)
    return spin_slot1

#4 spin slot line 2
def spin_slot_line_2():
    spin_slot2 = random.choice(symbols_list)
    return spin_slot2

#4 spin slot line 3
def spin_slot_line_3():
    spin_slot3 = random.choice(symbols_list)
    return spin_slot3

#4 spin slot line 4
def spin_slot_line_4():
    spin_slot4 = random.choice(symbols_list)
    return spin_slot4

#4 spin slot line 5
def spin_slot_line_5():
    spin_slot5 = random.choice(symbols_list)
    return spin_slot5

#4 spin slot line 6
def spin_slot_line_6():
    spin_slot6 = random.choice(symbols_list)
    return spin_slot6

#4 spin slot line 7
def spin_slot_line_7():
    spin_slot7 = random.choice(symbols_list)
    return spin_slot7

#4 spin slot line 8
def spin_slot_line_8():
    spin_slot8 = random.choice(symbols_list)
    return spin_slot8

#4 spin slot line 9
def spin_slot_line_9():
    spin_slot9 = random.choice(symbols_list)
    return spin_slot9

#5 results
def spin_slot_result1():
    slot1_result = spin_slot_line_1()
    slot2_result = spin_slot_line_2()
    slot3_result = spin_slot_line_3()

    slots_result1 = slot1_result + slot2_result + slot3_result
    print(slots_result1)
    return slots_result1

def spin_slot_result2():
    slot4_result = spin_slot_line_4()
    slot5_result = spin_slot_line_5()
    slot6_result = spin_slot_line_6()

    slots_result2 = slot4_result + slot5_result + slot6_result
    print(slots_result2)
    return slots_result2

def spin_slot_result3():
    slot7_result = spin_slot_line_7()
    slot8_result = spin_slot_line_8()
    slot9_result = spin_slot_line_9()

    slots_result3 = slot7_result + slot8_result + slot9_result
    print(slots_result3)
    return slots_result3

# calling functions
if __name__ == "__main__":
    total_deposit = get_deposit()
    bet_amount = get_bet_amount(total_deposit)
    number_of_lines = get_number_of_lines()

    result1 = spin_slot_result1()
    result2 = spin_slot_result2()
    result3 = spin_slot_result3()

    slots_result = result1 + result2 + result3

    #6 get win/loss. has for loop which cycles through each number of lines individually, 1 - 3.
    def determine_win_loss(slots_result, number_of_lines):
        for line in range(1, number_of_lines + 1):
            line_result = slots_result[line - 1::number_of_lines]
            if len(set(line_result)) == 1:
                print(f"You win on line {line}!")
            else:
                print(f"You lose on line {line}.")

    determine_win_loss(slots_result, number_of_lines)
