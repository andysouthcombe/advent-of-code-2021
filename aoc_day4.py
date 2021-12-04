class Card:
    def __init__(self):
        self.rows = []
        self.columns  = []
    
    def mark_number(self, number, line):
        return list(filter(lambda card_number: (card_number != number), line))
    
    def mark_card(self, number):
        for index, row in enumerate(self.rows):
            self.rows[index] = self.mark_number(number, row)
        for index, column in enumerate(self.columns):
            self.columns[index] = self.mark_number(number, column)

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
                for col in range(0,5):
                    column = []
                    for row in card.rows:
                        column.append(row[col])
                    card.columns.append(column)
                cards.append(card)
                card = Card()
                row_num_for_this_card = 0
            else:
                row_num_for_this_card +=1
        else:
            #skip empty line
            continue
    return cards


        