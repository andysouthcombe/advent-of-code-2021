signal_count_to_digit_dict = {
    2: 1,
    5: [2,3,5],
    4: 4,
    6: [0, 6, 9],
    3: 7,
    7: 8
}

def read_and_split_file(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        signals = []
        outputs = []
        for line in lines:
            signal_and_output = line.rstrip().split(' | ')
            signals.append(signal_and_output[0].split())
            outputs.append(signal_and_output[1].split())
        return signals, outputs

def count_digits_in_output_with_distinct_signal_count(output_list):
    counter = 0
    for output_line in output_list:
        for output in output_line:
            if isinstance(signal_count_to_digit_dict[len(output)], int):
                counter += 1
    return counter

def get_signals_for_number(known_signals,number):
    return [signal[0] for signal in known_signals if signal[1] == number][0]

def get_signals_with_distinct_counts(signals):
    return [signal for signal in signals if len(signal) in [2,4,3,7]]

def identify_signals_for_easy_numbers(distinct_signals):
    return [(signal, signal_count_to_digit_dict[len(signal)]) for signal in distinct_signals if len(signal) in [2,4,3,7]]

def identify_top_line(signals_for_one, signals_for_seven):
    return list(set(signals_for_seven) - set(signals_for_one))[0]

def find_known_digits_in_output(known_signals,output):
    known_digits = [None] * 4
    for index, digit in enumerate(output):
        for signal in known_signals:
            if set(digit) == set(signal[0]):
                known_digits[index] = signal[1]
    return known_digits
    #return [known_digit for known_digit in known_digits if known_digit is not None]
    
def find_number_six(easy_number_signals, signals):
    signal_for_one = set(get_signals_for_number(easy_number_signals, 1))
    for signal in signals:
        if len(signal) == 6:
            # the other digits with 6 signals(0,9) have all elements of signal for 1
            if not set(signal_for_one).issubset(signal):
                return signal
    return None

def find_number_nine(known_signals, signals,top_line_signal):
    signal_for_four = set(get_signals_for_number(known_signals, 4))
    for signal in signals:
        if len(signal) == 6:
            if len(set(signal) - set(signal_for_four) - set(top_line_signal)) == 1:
                return signal
    return None

def find_number_zero(known_signals, full_signals):
    signal_for_six = get_signals_for_number(known_signals, 6)
    signal_for_nine = get_signals_for_number(known_signals, 9)
    for signal in full_signals:
        if len(signal) == 6 and set(signal) != set(signal_for_six) and set(signal) != set(signal_for_nine):
            return signal

def decode_signals_and_output(signals, output):
    full_signals = signals + output
    known_signals = identify_signals_for_easy_numbers(full_signals)
    known_signals.append((find_number_six(known_signals, full_signals), 6))
    top_line_signal = identify_top_line(get_signals_for_number(known_signals, 1),get_signals_for_number(known_signals,7))
    known_signals.append((find_number_nine(known_signals, full_signals, top_line_signal), 9))
    known_signals.append((find_number_zero(known_signals, full_signals), 0))
    known_output_digits = find_known_digits_in_output(known_signals, output)
    return known_signals, known_output_digits

    



if __name__ == '__main__':
    signals, outputs = read_and_split_file('input\\day8.txt')
    for signal in signals:
        print(identify_signals_for_easy_numbers(signal))
