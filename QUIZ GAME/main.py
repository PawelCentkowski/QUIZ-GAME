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
        self.answers = self.get_answer(questions_file)
        self.correct_answers = self.get_correct_answer(questions_file)
        self.current_question = None
        self.current_answer = None
        self.current_answers = []
        self.option = None
        self.score = 0
        self.counter = 0
        self.create_widgets()
        self.next_question()
        self.x=""
        self.u_input = ""
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
        lines2n = []
        lines2 = []
        for x in range(10):
            lines2n.append(lines[x*6])
        #usuwa nowe linie bruh
        lines2 = [element.strip() for element in lines2n]
        #random.shuffle(lines2)
        return lines2
    
    def get_answer(self,file):
        answer_list = []  
        with open(file, "r",encoding="UTF-8") as f:
            lines = f.readlines()
        answer = [line.strip() for line in lines]
        if self.questions[0] in answer:
        #if 1==1:
         
            for x in range(10):
                question_index = answer.index(self.questions[x])
                a = answer[question_index+1]
                answer_list.append(a)
                b = answer[question_index+2]
                answer_list.append(b)
                c = answer[question_index+3]
                answer_list.append(c)
                d = answer[question_index+4]  
                answer_list.append(d)          
            #print(answer_list)
            return answer_list
     
    def create_widgets(self):
        self.label_question = tk.Label(self, text="", wraplength=800, font=("Arial", 25))
        self.label_question.config(background = "#555",padx=20,pady=20, height=5)
        self.label_question.pack()

        self.answers
        
        self.answerA =  self.answers[0]
        self.answerB =  self.answers[1]
        self.answerC =  self.answers[2]
        self.answerD =  self.answers[3]
        
        x = self.counter
        self.button1 = tk.Button(text=  self.answers[36-x*4], font=("Arial", 16), width=40, command=self.user_inputA,)
        self.button1.config(background="#fff", anchor="center",justify="center",)
        self.button1.pack(pady=5)

        self.button2 = tk.Button(text=  self.answers[37-x*4], font=("Arial", 16), width=40, command=self.user_inputB,)
        self.button2.config(background="#fff", anchor="center",justify="center")
        self.button2.pack(pady=5)

        self.button3 = tk.Button(text=  self.answers[38-x*4], font=("Arial", 16), width=40, command=self.user_inputC,)
        self.button3.config(background="#fff", anchor="center",justify="center")
        self.button3.pack(pady=5)

        self.button4 = tk.Button(text=  self.answers[39-x*4], font=("Arial", 16), width=40, command=self.user_inputD,)
        self.button4.config(background="#fff", anchor="center",justify="center")
        self.button4.pack(pady=5)
      

        #self.option_buttons = []
        #self.create_option_buttons()
        #self.current_answer = self.create_option_buttons()
        #self.create_option_buttons()

        self.button_check = tk.Button(self, text="Sprawdź", command=self.check_answer)
        self.button_check.pack(pady=5)

        self.button_next = tk.Button(self, text="Następne pytanie", command=self.next_question, state=tk.DISABLED)
        self.button_next.pack(pady=10)

        self.label_score = tk.Label(self, text="Wynik: 0")
        self.label_score.pack()

    def next_question(self):
        if self.questions:
            self.u_input = ""
            self.current_question = self.questions.pop()
            self.label_question.config(text=self.current_question)
            self.current_answers = self.answers
            self.counter+=1
            x = self.counter-1
            self.button1.config(text =self.answers[36-x*4],background="#fff")
            self.button2.config(text=  self.answers[37-x*4],background="#fff")
            self.button3.config(text=  self.answers[38-x*4],background="#fff")
            self.button4.config(text=  self.answers[39-x*4],background="#fff")
            #print(self.correct_answers)
            self.button_check.config(state=tk.NORMAL)
            self.button_next.config(state=tk.DISABLED) 
         
        else:
            messagebox.showinfo("Koniec gry", f"Twój wynik: {self.score}/10")
            self.destroy()

    def create_option_buttons(self,x=""):
        pass
        
    def user_inputA(self):
        print("a")
        self.button4.config(background="#fff")
        self.button3.config(background="#fff")
        self.button2.config(background="#fff")
        self.button1.config(background="#4040ff")
        self.u_input='a'
        return self.u_input
    def user_inputB(self):
        print("b")
        self.button4.config(background="#fff")
        self.button3.config(background="#fff")
        self.button1.config(background="#fff")
        self.button2.config(background="#4040ff")
        self.u_input='b'
        return self.u_input
    def user_inputC(self):
        print("c")
        self.button4.config(background="#fff")
        self.button1.config(background="#fff")
        self.button2.config(background="#fff")
        self.button3.config(background="#4040ff")
        self.u_input='c'
        return self.u_input
    def user_inputD(self):
        print("d")
        self.button1.config(background="#fff")
        self.button3.config(background="#fff")
        self.button2.config(background="#fff")
        self.button4.config(background="#4040ff")
        self.u_input='d'
        return self.u_input


    def get_correct_answer(self,file):
        correct_answers = []
        with open(file, "r",encoding="UTF-8") as f:
            lines = f.readlines()
        answer = [line.strip() for line in lines]
        if 1==1:
            for x in range(10):
                a = answer[5+x*6]
                correct_answers .append(a)       
            print(correct_answers)
            return correct_answers 
        
       

    def check_answer(self):
        #answer = self.entry_answer.get()
        answer = self.u_input
        #print(f"O TO JEST: {self.correct_answers[10-self.counter]}")
        if answer.lower() == self.correct_answers[10-self.counter]:
            self.score += 1
        self.label_score.config(text=f"Wynik: {self.score}")
        self.button_check.config(state=tk.DISABLED)
        self.button_next.config(state=tk.NORMAL)


if __name__ == "__main__":
    game = QuizGame("pytania.txt")
    game.mainloop()
