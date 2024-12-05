from tkinter import *
from Logic_VotingBooth import submit

class Gui:
    def __init__(self, window):
        self.window = window

        self.frame1 = Frame(self.window)
        self.top_label = Label(self.frame1, text='VOTING APPLICATION', font=("Arial", 35, 'bold'), fg='black')
        self.id_label = Label(self.frame1, text='ID', font=('Arial', 30))
        self.id_input = Entry(self.frame1, width=25, font=('Arial', 30))
        self.top_label.pack(side='top', padx=20)
        self.id_label.pack(side='left', pady = 20, padx = 20)
        self.id_input.pack(side='left', padx = 10, pady = 5)
        self.frame1.pack()

        self.frame2 = Frame(self.window)
        self.c_label = Label(self.frame2, text='CANDIDATES', font=('Arial', 35, 'bold'), fg='black')
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.r_1 = Radiobutton(self.frame2, text='Joe Biden', font=('Arial', 25),variable=self.radio_answer, value=1)
        self.r_2 = Radiobutton(self.frame2, text='Donald Trump', font=('Arial',25), variable=self.radio_answer, value=2)
        self.submit_button = Button(self.frame2, text = 'SUBMIT', font=('Arial', 35), command=self.submit)
        self.bottom_label = Label(self.frame2, text='Please Enter Your ID and Vote!', font=('Arial', 25), fg='green')
        self.c_label.pack(side='top', pady=20)
        self.r_1.pack(side='top')
        self.r_2.pack(side='top', pady=20)
        self.submit_button.pack(side='top', pady=50)
        self.bottom_label.pack(side='top', pady= 20)
        self.frame2.pack()

    def submit(self):
        voter_id: str = self.id_input.get()
        person_chose: int = self.radio_answer.get()

        submit(voter_id, person_chose, self.radio_answer, self.id_input, self.bottom_label )

