class Card:
    def __init__(self):
        self.rows = []
        self.columns  = []
    
    def mark_number(self, number, line):
        return list(filter(lambda card_number: (card_number != number), line))
    
    def mark_card_and_see_if_winner(self, number):
        for index, row in enumerate(self.rows):
            self.rows[index] = self.mark_number(number, row)
            if self.check_for_winner(self.rows[index]):
                return True
        for index, column in enumerate(self.columns):
            self.columns[index] = self.mark_number(number, column)
            if self.check_for_winner(self.columns[index]):
                return True
        return False

    def check_for_winner(self, line):
        return len(line) == 0
    
    def sum_remaining_numbers(self):
        sum_remaining = 0 
        for row in self.rows:
            sum_remaining += sum(row)
        return sum_remaining

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

# def play_bingo(filename):
#     cards = read_cards(filename)
#     numbers = read_numbers(filename)
#     for number in numbers:
#         for card in cards:
#             have_we_got_a_winner = card.mark_card_and_see_if_winner(number)
#             if have_we_got_a_winner:


        