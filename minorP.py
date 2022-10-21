#import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import os



#initializing window

root = Tk()
root.geometry("550x400")
root.resizable(0,0)
root.configure(bg='light goldenrod')
root.title("TEXT TO SPEECH")


#--> heading

Label(root, text = "TEXT-TO-SPEECH",
      font = "arial 20 bold",
      bg = 'light goldenrod',
      fg = 'red4').pack()
Label(text = "copyright (c) 2021 | Pankhuri, Damini, Roushan ",
      font = 'arial 7 italic',
      bg = 'White smoke',
      width = '500').pack(side = 'bottom')



#--> text variable

Msg = StringVar()


#--> label

Label(root,
      text = "Enter Text",
      font = 'arial 15 bold',
      bg = 'red4',
      fg = 'light goldenrod').pack()



#--> entry

entry_field = Entry(root, textvar = Msg, width = '67')
entry_field.place(x=75, y=100)



#declare functions

#--> function to convert text to speech

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message, lang = 'en', slow = False)
    speech.save('Drop.mp3')
    playsound('Drop.mp3')
    os.remove('Drop.mp3')




#--> funtion to exit

def Exit():
    root.destroy()




#--> function to reset

def Reset():
    Msg.set("")





#define buttons

Button(root,
       text = "PLAY", font = 'arial 15 bold', command = Text_to_speech,
       fg = 'green4', width = '6').place(x=140, y=140)

Button(root,
       font = 'arial 15 bold', text = "EXIT", width = '6',
       command = Exit, fg = 'red4').place(x=225, y=140)

Button(root, font = 'arial 15 bold', text = "RESET", width = '6',
       command = Reset, fg = 'royal blue4').place(x=310, y=140)





#infinite loop

root.mainloop()
