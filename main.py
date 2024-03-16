from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data=pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")          #we need full file when we need rerun our code
    to_learn=original_data.to_dict(orient="records")            #if original data not found we gonna to this
else:
    to_learn=data.to_dict(orient="records")             #gives us a dict of our both french and english key in one dict


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_back_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)          #creating seprate file for words which we dont know which need to be learn
    data.to_csv("data/words_to_learn.csv",index=False)      #we our adding index false bcz when our new files
                                                                      #are being created dont have over and over indexes and turn to no index
    next_card()

window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)       #for time gap

canvas=Canvas(width=800,height=526)
front_image=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=front_image)          #the first 2 args are basically padding provided to our
                                                        # grid and thats basically half of our canvas width and hgt
card_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="images/right.png")
known_button=Button(image=check_image,highlightthickness=0,command=next_card)
known_button.grid(row=1,column=1)

next_card()             #we are calling fxn bcz when our app first run it dont show us title and word it directly get
                        # started with french and words, we can even erase title and word from card_title&word bcz they
                        #are not at all in use





window.mainloop()

