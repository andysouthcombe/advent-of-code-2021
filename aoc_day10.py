open_to_closing_chars = {
                    '(': ')',
                    '<': '>',
                    '[': ']',
                    '{': '}'
                }

closing_to_open_chars = {value:key for key, value in open_to_closing_chars.items()}

def get_invalid_closing_character(input):
    open_chars = []
    close_chars = []
    for char in input:
        if char in open_to_closing_chars:
            open_chars.append(char)
        elif closing_to_open_chars[char] not in open_chars:
            return char
        else:
            close_chars.append(char)
    if (len(open_chars) == len(close_chars)):
        return None
