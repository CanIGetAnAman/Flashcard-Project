from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    updated_words_df = pandas.read_csv("words_to_learn.csv")
    updated_to_learn = updated_words_df.to_dict(orient="records")
except FileNotFoundError:
    updated_words_df = None
    updated_to_learn = None

words_df = pandas.read_csv("data/french_words.csv")
to_learn = words_df.to_dict(orient="records")
random_card = None
random_french = None
random_english = None


def click_green():
    global updated_to_learn
    if random_card is None:
        next_card()
    elif updated_to_learn is None:
        updated_to_learn = to_learn
    else:
        updated_to_learn = [i for i in updated_to_learn if not (i['French'] == random_french)]
        to_learn_dict = pandas.DataFrame(updated_to_learn)
        to_learn_dict.to_csv("words_to_learn.csv", index=False)
        next_card()


def next_card():
    global random_card
    global random_french
    global random_english
    if updated_to_learn is None:
        random_card = random.choice(to_learn)
        random_french = random_card["French"]
        random_english = random_card["English"]
        canvas.itemconfig(canvas_img, image=front_img)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_text, text=random_french, fill="black")
        window.after(3000, func=flip_card)
    else:
        try:
            random_card = random.choice(updated_to_learn)
        except IndexError:
            canvas.itemconfig(card_title, text="Congrats", fill="black")
            canvas.itemconfig(card_text, text="You did them all!", fill="black")
        else:
            random_french = random_card["French"]
            random_english = random_card["English"]
            canvas.itemconfig(canvas_img, image=front_img)
            canvas.itemconfig(card_title, text="French", fill="black")
            canvas.itemconfig(card_text, text=random_french, fill="black")
            window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=random_english, fill="white")


# Create UI
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 130, text="Title", font=("Welcome", 40, "italic"))
card_text = canvas.create_text(400, 263, text="Press any button to begin", font=("Arial", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create DataFrame with flashcard words
# Define a function that will pull a random french word and its translation from the DF
# Puts random French word on card when you click either button


# Create Buttons
red_img = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_img, highlightthickness=0, command=next_card)
red_button.grid(column=0, row=1)

green_img = PhotoImage(file="images/right.png")
green_button = Button(image=green_img, highlightthickness=0, command=click_green)
green_button.grid(column=1, row=1)

# def random_words():
#     words_df = pandas.read_csv("data/french_words.csv")
#     random_row = words_df.sample(ignore_index=True)
#     random_french = random_row["French"][0]
#     translation = random_row["English"][0]


window.mainloop()
