from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

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

# answer = bot.get_response("What is your name?")
# print(answer)
# print('You can ask me your questions!')

# while True:
#     query = input()
#     if query == 'Exit':
#         break
#     answer = bot.get_response(query)
#     print('Bot : ',answer)

main = Tk()

main.geometry("500x700")

main.title("My Chat Bot")

img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack()


def ask_from_bot():
    query = textF.get()
    answer = bot.get_response(query)
    msgs.insert(END, "You: " + query)
    msgs.insert(END, "Bot: " + str(answer))
    textF.delete(0, END)


frame = Frame(main)

scv = Scrollbar(frame)

sch = Scrollbar(frame)

msgs = Listbox(frame, font=("Verdana", 10), width=150, height=20)

scv.pack(side=RIGHT, fill=Y)
sch.pack(side=BOTTOM, fill=X)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))

textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask to Bot", font=("Verdana", 20), command=ask_from_bot)

btn.pack()

main.mainloop()
