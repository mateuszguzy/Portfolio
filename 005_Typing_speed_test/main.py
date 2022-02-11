from tkinter import *
from tkinter import messagebox
from word_bank import word_bank
import time
import random


main_window = Tk()

# ------ CONSTANTS
# --- COLORS
COLOR_1 = "#21325E"
COLOR_2 = "#3E497A"
COLOR_3 = "#F1D00A"
COLOR_4 = "#F0F0F0"
# --- FONTS
TITLE_FONT = ("Quicksand", 20, "bold")
WORDS_FONT = ("Quicksand", 15,)
# --- WINDOW SIZE
MAIN_WINDOW_WIDTH = 600
MAIN_WINDOW_HEIGHT = 600
# --- VARIABLES
WORDS_TO_CHECK = list()
USER_WORDS = list()
START_TIME = int()
END_TIME = int()
with open("high_score.txt", "r") as file:
    CURRENT_HIGH_SCORE = int(file.readline())


# ------ MAIN WINDOW LAYOUT
main_window.title("Typing Speed Test")
main_window.config(padx=10, pady=10, bg=COLOR_1)
main_window.minsize(width=MAIN_WINDOW_WIDTH, height=MAIN_WINDOW_HEIGHT)
title = Label(main_window, text="TYPING SPEED TEST", bg=COLOR_1, fg=COLOR_4, font=TITLE_FONT)
canvas = Canvas(main_window, width=MAIN_WINDOW_WIDTH - 20, height=275, bg=COLOR_2, highlightthickness=0)


def start_test():
    # reset global vars and clear word table with each test restart
    global USER_WORDS, WORDS_TO_CHECK
    USER_WORDS = list()
    WORDS_TO_CHECK = list()
    canvas.itemconfig(tagOrId="canvas_text", text="")
    # set timer giving user time to prepare
    timer(3)
    # set focus on entry field and listen for spacebar key to confirm written word
    text_input.focus_set()
    text_input.bind("<KeyPress-space>", clear)


def timer(t):
    global START_TIME
    # countdown three seconds until start of the test
    if t > 0:
        canvas.itemconfig(timer_text, text=t)
        main_window.after(1000, timer, t-1)
    # when countdown ends, clear the text and show test words
    else:
        canvas.itemconfig(timer_text, text="")
        prepare_wordlist()
        # take present time to count 60 seconds of the test
        minutes = time.strftime("%M")
        sec = time.strftime("%S")
        START_TIME = int(minutes) * 60 + int(sec)


def get_input():
    global USER_WORDS
    # get sanitized user input
    USER_WORDS.append(text_input.get().strip())


def clear(key):
    global END_TIME, START_TIME
    # with every spacebar press run this function and count if given test time has passed
    get_input()
    minutes = time.strftime("%M")
    sec = time.strftime("%S")
    END_TIME = int(minutes) * 60 + int(sec)
    # 60 represents test length (for debug 10 is enough)
    if END_TIME >= START_TIME + 60:
        # take necessary vars from score checking function
        score, new_record, mistakes = check_score()
        # set beginning of a message with score only
        info_text = f"Your WPM score: {score}"
        # in case user sets a new record add info about it
        if new_record is True:
            info_text += f"\n\nNEW RECORD!"
        # if there are no mistakes add info about it
        if len(mistakes) == 0:
            info_text += "\n\nNO MISTAKES!"
            messagebox.showinfo("SCORE", info_text)
            # if there are no mistakes to show, clear canvas
            canvas.itemconfig(tagOrId="canvas_text", text="")
        # if there are mistakes, check if user wants to see them
        else:
            show_mistakes = messagebox.askyesno("SCORE", info_text + "\n\nDo you want to see the mistakes?")
            # if yes fill canvas with mistakes, if not clear canvas
            if show_mistakes:
                canvas.itemconfig(tagOrId="canvas_text", text=mistakes)
            else:
                canvas.itemconfig(tagOrId="canvas_text", text="")
    # clear entry field for another user input
    text_input.delete(0, END)


def check_score():
    global WORDS_TO_CHECK, USER_WORDS, CURRENT_HIGH_SCORE
    # reset vars
    score = 0
    # mistakes_list = list()
    mistakes_list = str()
    # cross-check words written by user and from word bank looking for mistakes
    for i, k in zip(WORDS_TO_CHECK[:len(USER_WORDS)], USER_WORDS):
        # if there's no mistake add to user score
        if i == k:
            score += 1
        # if there's mistake add it to mistakes list
        else:
            mistakes_list += f"({i} - {k})   "
    # default state is no new high score
    new_record = False
    # if user surpasses current high score, write it in a txt file and change new_record var
    if score > CURRENT_HIGH_SCORE:
        CURRENT_HIGH_SCORE = score
        # update GUI view of current high score
        current_high_score.config(text=CURRENT_HIGH_SCORE)
        new_record = True
        with open("high_score.txt", "w") as writable_file:
            writable_file.write(str(score))
    return score, new_record, mistakes_list


def prepare_wordlist():
    global WORDS_TO_CHECK
    # for every test loop prepare clear test wordlist
    wordlist = str()
    # take words from word_bank.py file
    words = word_bank
    # show user 90 words to write
    for i in range(90):
        # select random word from wordlist so every test list is different
        letter = random.choice(words)
        # add selected word to both WORDS_TO_CHECK list and wordlist string
        WORDS_TO_CHECK.append(letter.lower())
        wordlist += letter.lower() + "   "
        # remove word from the poll so there are no doubles
        words.remove(letter)
    # add word back to the word_bank list so in another loop there is complete word bank again
    for letter in WORDS_TO_CHECK:
        word_bank.append(letter)
    # when 90 words are selected show them to user in canvas
    canvas.create_text(5, 0, text=wordlist, anchor=NW, width=MAIN_WINDOW_WIDTH - 30, justify=LEFT, font=WORDS_FONT,
                       tags="canvas_text")


# ------ MAIN PAGE LAYOUT
timer_text = canvas.create_text(300, 135, text="PREPARE", font=("Quicksand", 70, "bold"), tags="timer")
text_input = Entry(main_window, bg=COLOR_2, fg=COLOR_4, font=WORDS_FONT, highlightcolor=COLOR_4, justify=CENTER, bd=5)
start_button = Button(main_window, text="START!", bg=COLOR_2, fg=COLOR_3, command=start_test,
                      font=TITLE_FONT, highlightthickness=0)
current_high_score_label = Label(main_window, text="High score:", bg=COLOR_1, fg=COLOR_4, font=TITLE_FONT)
current_high_score = Label(main_window, text=CURRENT_HIGH_SCORE, bg=COLOR_1, fg=COLOR_3, font=TITLE_FONT)

# ------ POSITIONING
title.grid(row=1, column=0, columnspan=3, pady=20)
canvas.grid(row=2, column=0, columnspan=3, pady=20)
text_input.grid(row=3, column=0, columnspan=3, pady=20)
start_button.grid(row=4, column=2, pady=20)
current_high_score_label.grid(row=4, column=0, sticky=N)
current_high_score.grid(row=4, column=0, sticky=S)

main_window.mainloop()
