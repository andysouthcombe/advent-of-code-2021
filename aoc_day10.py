open_to_closing_chars = {
                    '(': ')',
                    '<': '>',
                    '[': ']',
                    '{': '}'
                }

closing_to_open_chars = {value:key for key, value in open_to_closing_chars.items()}

def get_invalid_closing_character(input):
    open_chars = []
    for char in input:
        if char in open_to_closing_chars:
            open_chars.append(char)
            continue
        try:
            open_chars.remove(closing_to_open_chars[char])
        except(ValueError):
            return char
    return None
