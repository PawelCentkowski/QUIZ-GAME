import tkinter as tk
from tkinter import messagebox
import random
from tkinter.ttk import *

class QuizGame(tk.Tk):
    def __init__(self, questions_file):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("1600x800")
        self.p1 =  tk.PhotoImage(file = 'civ_logo.png')
        self.config(background="#555")
        # Setting icon of master window
        self.iconphoto(False, self.p1)
        self.questions = self.load_questions(questions_file)
        self.current_question = None
        self.score = 0
        self.create_widgets()
        self.next_question()
        #self.lines2 = []
        #self.question = []
        #self.answer_list = []
    #dowload screen res and justifies the application window
    def screen_initiator( self):
        self.window_width = 1600
        self.window_height = 800
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.center_x = int(self.screen_width/2-self.window_width/2)
        self.center_y = int(self.screen_height/2-self.window_height/2)
        self.geometry(f"{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}")

        
    def load_questions(self, file):
        with open(file, "r",encoding="UTF-8") as f:
            lines = f.readlines()
        question = [line.strip() for line in lines]
        lines2 = []
        for x in range(10):
            lines2.append(lines[x*6])
        random.shuffle(lines2)
        return lines2
    """""
    def get_answer(self):

        lines = question
       # print(self.lines2)
       # print("pod tym inna lista")
        #print(self.lines)
        if lines2[0] in lines:
            for x in range(10):
                question_index = lines.index(lines2[x])
                a = lines[question_index+1]
                b = lines[question_index+2]
                c = lines[question_index+3]
                d = lines[question_index+4]     
            answer_list = [a, b, c, d]     
            return answer_list
        """""
    def create_widgets(self):
        self.label_question = tk.Label(self, text="", wraplength=800, font=("Arial", 25))
        self.label_question.config(background = "#555",padx=20,pady=20, height=5)
        self.label_question.pack()

        #self.entry_answer = tk.Entry(self)
        #self.entry_answer.pack(pady=10)
        
        #self.question_label = tk.Label(text="", font=("Arial", 20))
        #self.question_label.pack(pady=20)
        #self.get_answer()
        self.option_buttons = []
        self.create_option_buttons()
        

        self.button_check = tk.Button(self, text="Sprawdź", command=self.check_answer)
        self.button_check.pack(pady=5)

        self.button_next = tk.Button(self, text="Następne pytanie", command=self.next_question, state=tk.DISABLED)
        self.button_next.pack(pady=10)

        self.label_score = tk.Label(self, text="Wynik: 0")
        self.label_score.pack()

    def next_question(self):
        if self.questions:
            self.current_question = self.questions.pop()
            self.label_question.config(text=self.current_question)
           #self.entry_answer.delete(0, tk.END)
            self.button_check.config(state=tk.NORMAL)
            self.button_next.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Koniec gry", f"Twój wynik: {self.score}/{len(self.questions)+self.score}")
            self.destroy()

    def create_option_buttons(self):

        
        
        listka = ["a","b","c","d"]
        for _ in range(4):
            button = tk.Button(text= listka[_], font=("Arial", 16), width=40)#-1
            button.config(background="#fff")
            button.pack(pady=5)
            self.option_buttons.append(button)

    def check_answer(self):
        #answer = self.entry_answer.get()
        answer = "a"
        if answer.lower() == "tak":
            self.score += 1
        self.label_score.config(text=f"Wynik: {self.score}")
        self.button_check.config(state=tk.DISABLED)
        self.button_next.config(state=tk.NORMAL)


if __name__ == "__main__":
    game = QuizGame("pytania.txt")
    game.mainloop()
