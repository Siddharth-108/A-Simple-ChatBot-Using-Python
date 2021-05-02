from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.CRITICAL)

bot = ChatBot("My_Bot")
convo = ['Hello',
         'Hi, there!',
         'What is your name?',
         'My name is Bot007, I am created by ToP_GuN™',
         'How are you?',
         'I am Great!',
         'In which city do you live?',
         'I live in Pune.',
         'In which language do you speak?',
         'I am comfortable in English on frontend & in Python on backend:)',
         'Bye!',
         'Thankyou!']

trainer = ListTrainer(bot)

trainer.train(convo)

main = Tk()

main.geometry("500x700")

main.title("My Chat Bot")

img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack()


def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Your Bot is Listening, speak something!")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer = bot.get_response(query)
    msgs.insert(END, "You: " + query)
    msgs.insert(END, "Bot: " + str(answer))
    speak(answer)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

scv = Scrollbar(frame)

# sch = Scrollbar(frame)

msgs = Listbox(frame, font=("Verdana", 10), width=150, height=20, yscrollcommand=scv.set)

scv.pack(side=RIGHT, fill=Y)
# sch.pack(side=BOTTOM, fill=X)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))

textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask to Bot", font=("Verdana", 20), command=ask_from_bot)

btn.pack()


def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()
