class Card:
    def __init__(self):
        self.rows = []
    
    def mark_numbers(self, numbers, line):
        return list(filter(lambda card_number: (card_number not in numbers), line))

    def check_for_winner(self, numbers):
        for line in self.rows + self.get_columns():
            if len(self.mark_numbers(numbers, line)) == 0:
                return True
        return False
    
    def sum_remaining_numbers(self, numbers):
        return sum([sum(self.mark_numbers(numbers, line)) for line in self.rows])
        
    
    def get_columns(self):
        return [list(column) for column in zip(*self.rows)]

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

def play_bingo(cards_filename, numbers_filename):
    cards = read_cards(cards_filename)
    numbers = read_numbers(numbers_filename)
    for number_index in range(0, len(numbers)):
        for card in cards:
            numbers_sliced = numbers[0:number_index + 1]
            if card.check_for_winner(numbers_sliced):
                print(f'we have a winner! last number: {numbers_sliced[-1]} remaining on card: {card.sum_remaining_numbers(numbers_sliced)}')
                return True

def last_to_win(cards_filename, numbers_filename):
    cards = read_cards(cards_filename)
    numbers = read_numbers(numbers_filename)
    cards_that_won = []
    while len(cards) > 0:
        for number_index in range(0, len(numbers)):
            for card_index, card in enumerate(cards):
                numbers_sliced = numbers[0:number_index + 1]
                if card.check_for_winner(numbers_sliced):
                    cards_that_won.append((card.sum_remaining_numbers(numbers_sliced), numbers_sliced[-1]))
                    cards.pop(card_index)
    print(f'we have a winner! last number: {cards_that_won[-1][1]} remaining on card: {cards_that_won[-1][0]}')
    return True


if __name__ == '__main__':
    play_bingo('input\\day_4_test_cards.txt','input\\day_4_test_numbers.txt')
    play_bingo('input\\day_4_cards.txt','input\\day_4_numbers.txt')
    last_to_win('input\\day_4_test_cards.txt','input\\day_4_test_numbers.txt')
    last_to_win('input\\day_4_cards.txt','input\\day_4_numbers.txt')