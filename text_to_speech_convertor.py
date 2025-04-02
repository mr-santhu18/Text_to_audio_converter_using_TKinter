from tkinter import *
from gtts import gTTS

import os

# create a root window
root = Tk()

# freame 1 creation
frame1 = Frame(root, bg="black", height="150")
frame1.pack(fill=X)
# frame 2 creation
frame2= Frame(root,bg="red", height="750")
frame2.pack(fill=X)

# label widget in frame1
Label=Label(frame1, text="TEXT TO AUDIO", font="bold, 30", bg="red")
Label.place(x=180, y=70)

# entry widget
Entry=Entry(frame2, width=45, bd=4, font=14)
Entry.place(x=130, y=52)
Entry.insert(0, "")

# define function for converting text to audio

def play():
    language="en"

    myobj=gTTS(text=Entry.get(), lang=language, slow=False)
    myobj.save("converted.wav")
    os.system("converted.wav")

# button widget

btn=Button(frame2, text="SUBMIT", width="15", pady=10, font="bold,15", command=play, bg="green")
btn.place(x=150, y=130)

root.title("TEXT_TO_AUDIO_CONVERTOR")

root.geometry("650x550+350+200")



root.mainloop()

