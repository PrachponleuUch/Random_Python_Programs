import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy = [:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
            
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): #transposing
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=' | ') # end (choose what to end with.. default is \n)
            else:
                print(column[row], end='')
                print() #print new line

def Deposit():
    while True:
        amount = input("Deposit Amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_line():
    while True:
        lines = input(f"Enter number of lines (1 - {str(MAX_LINES)}): ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter bet amount ({str(MIN_BET)} - {str(MAX_BET)}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return bet

def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to proceed.\nYour current balance is {balance}")
        else:
            break                
    print(f"You are betting ${bet} on {lines} lines.\nTotal bet: ${total_bet}.")
    
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    
    return winnings - total_bet

def main():
    balance = Deposit()
    while True:
        print(f"Current balance is ${balance}")
        user_input = input("Press enter to play (q to quit).")
        if user_input == "q":
            break;
        balance += spin(balance)
        
    print(f"You left with ${balance}")

main()