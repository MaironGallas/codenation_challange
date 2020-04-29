def julio_cesar_decoder(number, code_text):
    char_decoded = []
    for letter in code_text:
        char = ord(letter)
        if char == 32:
            ascii_number = 32
        elif char == 46:
            ascii_number = 46
        elif (char - number) < 97:
            ascii_number = (((char - number) + 122) - 97) + 1
        else:
            ascii_number = char - number
        char_decoded.append(chr(ascii_number))
    return "".join(char_decoded)