class Card:
    def __init__(self):
        self.rows = []
    

def read_file(filename):
    with open(filename,'r') as f:
        return f.read().splitlines()

def read_numbers(filename):
    raw_numbers = read_file(filename)
    return [int(num) for num in raw_numbers[0].split(',')]

def read_cards(filename):
    raw_cards = read_file(filename)
    cards = []
    card = Card()
    row_num_for_this_card = 0
    for line in raw_cards:
        if len(line) > 0: 
            card.rows.append([int(number) for number in line.split()])
            if  row_num_for_this_card == 4:
                cards.append(card)
                card = Card()
                row_num_for_this_card = 0
            else:
                row_num_for_this_card +=1
        else:
            #skip empty line
            continue

    return cards

