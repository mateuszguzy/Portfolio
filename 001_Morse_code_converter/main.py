# MORSE CODE CONVERTER

# prepare converter dictionary letter:morse_code_translation
converter = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}


def main():
    # welcome info and program clarification
    print(simple_title_frame("Morse Code Converter"))
    print("(1) Convert sentence to Morse Code")
    print("(2) Convert Morse Code to Latin alphabet (to be added)")
    print("(3) Quit\n")
    mode = input("Please choose translation mode:\n")
    if mode == "1":
        translation = latin_to_morse()
        print(f"Original sentence:\n{translation[0]}\n\nTranslated sentence:\n{translation[1]}\n")
    elif mode == "2":
        translation = morse_to_latin()
        print(f"Original sentence:\n{translation[0]}\n\nTranslated sentence:\n{translation[1]}\n")
    elif mode == "3":
        quit()
    else:
        main()
    next_translate = input("Do you want to translate another sentence?\n(1) Yes | (2) Quit\n")
    if next_translate == "1":
        main()
    else:
        quit()


def latin_to_morse():
    # take user input of sentence to translate
    sentence = user_input()
    # separate user input into words, and create list out of it
    words = sentence.split(" ")
    letter_space = 3 * " "
    word_space = 6 * " "
    new_sentence = str()
    # last letter in word needs no "letter space", so counter determine for which letter omit the space
    counter = 0
    # in every word check every letter (ignore case) in dictionary and make new string with morse code
    for word in words:
        for letter in word:
            # after every letter add three spaces (but last in word)
            new_sentence += converter[letter.upper()]
            if counter != len(word) - 1:
                new_sentence += letter_space
            counter += 1
        # after each word add six spaces
        new_sentence += word_space
    return sentence, new_sentence


def morse_to_latin():
    print(simple_title_frame("!!! WARNING !!!"))
    print("\nBetween letters there are three spaces, between words six spaces.")
    sentence = user_input()
    keys = list(converter.keys())
    values = list(converter.values())
    words = sentence.split(6 * " ")
    new_words_list = list()
    new_sentence = str()
    for word in words:
        letters = word.split(3 * " ")
        word = str()
        for letter in letters:
            index_value = values.index(letter)
            letter = keys[index_value]
            word += letter
        new_words_list.append(word)
    for word in new_words_list:
        new_sentence += word + " "
    return sentence, new_sentence.strip()


def user_input():
    sentence = input("Please write message to translate:\n")
    print(f"Is that the message you want to translate?\n{sentence}")
    confirmation = input("(1) Yes | (2) No | (3) Quit\n")
    if confirmation == "1":
        return sentence
    elif confirmation == "2":
        latin_to_morse()
    elif confirmation == "3":
        quit()
    else:
        main()


def simple_title_frame(text):
    text_length = len(text)
    frame_symbol = "#"
    top_bar = ((2 * text_length) * frame_symbol) + "\n"
    middle_bar = frame_symbol + ((int(text_length / 2) - 1) * " ") + text + ((int(text_length / 2) - 1) * " ") + frame_symbol + "\n"
    bottom_bar = ((2 * text_length) * frame_symbol)
    frame = top_bar + middle_bar + bottom_bar
    return frame


if __name__ == "__main__":
    main()
