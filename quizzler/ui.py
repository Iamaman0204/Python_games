import tkinter.messagebox
from tkinter import *
from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ["Arial", 20, "italic"]


class Quizzler:
    def __init__(self,quizz_brain:QuizBrain):
        self.quizz_brain= quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)

        self.score = Label(background=THEME_COLOR,text="score:0",fg='white')
        self.score.grid(column=1, row=0)

        self.card = Canvas(background='white',height=250,width=300)
        self.question=self.card.create_text(150,125,width=280,text = "The game is on")
        self.card.grid(columnspan=2, row=1,column=0)

        photoImageRight = PhotoImage(file="images/true.png")
        photoImageWrong = PhotoImage(file='images/false.png')

        self.right = Button(image=photoImageRight,highlightthickness=0,command=self.check_right)
        self.right.grid(row=2,column=0,pady=20)

        self.wrong = Button(image=photoImageWrong,highlightthickness=0,command=self.check_wrong)
        self.wrong.grid(row=2,column=1,pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quizz_brain.still_has_questions():
            question = self.quizz_brain.next_question()
            self.score.config(text=f"score: {self.quizz_brain.score}")
            self.card.itemconfig(self.question, text=question)
            self.card.config(bg='white')
            self.right.config(state="normal")
            self.wrong.config(state='normal')
        else:
            self.card.itemconfig(self.question,text=f"Your Final Score:{self.quizz_brain.score}/10\nPlay Again")
            self.right.config(state="disabled")
            self.wrong.config(state='disabled')
            tkinter.messagebox.askyesno(title='Quizzler',message='Do you want to play')


    def check_right(self):
        check=self.quizz_brain.check_answer('True')
        self.update_card(check)

    def check_wrong(self):
        check=self.quizz_brain.check_answer('False')
        self.update_card(check)

    def update_card(self,is_right):
        if is_right:
            self.card.config(bg='green')
        else:
            self.card.config(bg='red')
        self.right.config(state="disabled")
        self.wrong.config(state='disabled')
        self.window.after(1000,self.next_question)


