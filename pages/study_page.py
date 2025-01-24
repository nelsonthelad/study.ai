import customtkinter as ctk
import json
from save_processing import update_best_score
from save_processing import get_file_data
from save_processing import update_attemtps

class StudyPage(ctk.CTkFrame):
    def __init__(self, master, filename):
        super().__init__(master)
        self.id = 0
        self.score = []
        self.finished = False
        self.filename = filename

        self.data = get_file_data(filename)
        if self.data is None:
             print("No data")
             return
        
        self.numquestions = self.get_num_questions(data=self.data)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.question_frame = QuestionFrame(self, id=self.id, data=self.data)
        self.question_frame.grid(row=0, column=0, stick="nsew")

        self.submit_button = ctk.CTkButton(
            self,
            text="Submit",
            command=self.check_answer
        )
        self.submit_button.grid(row=1, column=0, padx=15, pady=15)

        self.next_button = ctk.CTkButton(
            self,
            text="Next",
            command=self.update_question
        )
        self.next_button.grid(row=1, column=0, padx=15, pady=15, sticky="e")

        self.quit_button = ctk.CTkButton(
            self,
            text="Quit",
            command=self.quit
        )
        self.quit_button.grid(row=1, column=0, padx=15, pady=15, sticky="w")

    def get_num_questions(self, data=None):
        if data is None:
            print("No Data")
            return None
        
        if isinstance(data, str):
            data = json.loads(data)
        
        return len(data['questions'])
    
    def update_question(self):
        if self.id + 1 < self.numquestions: 
            self.id += 1
            self.score.append(self.question_frame.result)
            self.question_frame.destroy() 
            self.question_frame = QuestionFrame(self, id=self.id, data=self.data)
            self.question_frame.grid(row=0, column=0, stick="nsew")
        else:
            self.finished = True
            self.score.append(self.question_frame.result)
            self.results_frame = ResultsFrame(self, data=self.data, score=self.score)
            self.question_frame.destroy()
            self.results_frame.grid(row=0, column=0, stick="nsew")
            self.submit_button.destroy()
            self.next_button.destroy()
            self.quit_button.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")
    
    def check_answer(self):
        self.question_frame.check_answer()

    def quit(self):
        if self.finished:
            update_best_score(self.filename, self.score)
            update_attemtps(self.filename)

        from .saved_page import SavedPage
        self.master.show_frame(SavedPage)
        

class QuestionFrame(ctk.CTkFrame):
    def __init__(self, master, id, data):
        super().__init__(master)

        self.data = data
        self.question_id = id
        self.checkboxes = []
        self.selected_answer = None
        self.answered = False
        self.result = None

        self.question = self.get_question(self.data, self.question_id)

        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.question_label = ctk.CTkLabel(
            self,
            text=self.question,
            font=ctk.CTkFont(size=28),
            wraplength=600,
            fg_color="#3b3b3b",  
            corner_radius=8,           
            anchor="center",
        )
        self.question_label.grid(row=0, column=0, stick="nsew", pady=15, padx=15)

        self.create_answer_options()

    def create_answer_options(self):
        self.answers = self.get_answers(self.data, self.question_id)
        
        for checkbox in self.checkboxes:
            checkbox.destroy()
        self.checkboxes = []

        for i in range(len(self.answers)):
            checkbox = ctk.CTkCheckBox(
                self,
                text=self.answers[i],
                font=ctk.CTkFont(size=28),
                command=lambda i=i: self.select_checkbox(i)
            )
            checkbox.grid(row=i+1, column=0, padx=40, pady=15, sticky="w")
            self.checkboxes.append(checkbox)

    def select_checkbox(self, selected_index):
        if not self.answered:  
            for i, checkbox in enumerate(self.checkboxes):
                if i != selected_index:
                    checkbox.deselect()
                else:
                    checkbox.select()
                    self.selected_answer = selected_index

    def get_question(self, data, id):
        if data is None or 'questions' not in data:
            return None
        
        return data['questions'][id]['question']
        
    def get_answers(self, data, id):
        return data['questions'][id]['options']
    
    def check_answer(self):
        if self.selected_answer is None or self.answered:
            return

        self.answered = True  
        data = self.data
        id = self.question_id
        selected = data['questions'][id]['options'][self.selected_answer]

        if data['questions'][id]['answer'] == selected:
            self.result = "Correct!"
        else:
            self.result = "Incorrect!"

        for checkbox in self.checkboxes:
            checkbox.grid_forget()
    
        self.result_label = ctk.CTkLabel(
            self,
            text=self.result,
            font=ctk.CTkFont(size=42),
            fg_color="#3b3b3b",  
            corner_radius=8,           
            anchor="center",
        )
        self.result_label.grid(row=3, column=0, pady=100, padx=100, sticky="nsew")


class ResultsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, data, score):
        super().__init__(master, scrollbar_button_color="#333333", scrollbar_button_hover_color="#333333")

        self.data = data

        self.score = self.get_score(score=score)

        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.result_label = ctk.CTkLabel(
            self,
            text="Attempt Score: " + self.score,
            font=ctk.CTkFont(size=32),
            fg_color="#3b3b3b",  
            corner_radius=8,           
            anchor="center",
        )
        self.result_label.grid(row=0, column=0, pady=15, padx=15, sticky="nsew")

        i = 0
        color = None
        for i in range(len(score)):
            if score[i] == "Correct!":
                color = "green"
            else:
                color = "red"

            question_label = ctk.CTkLabel(
                self,
                text=f"({i + 1}) {score[i]}",
                font=ctk.CTkFont(size=12),
                wraplength=650,
                justify="center",
                text_color=color
            )
            question_label.grid(row=i+1, pady=15, padx=15)
            i += 1

    def get_score(self, score):
        true_counter = 0
        num_questions = len(score)

        for i in range(len(score)):
            if score[i] == "Correct!":
                true_counter += 1

        return f"{true_counter}/{num_questions}"

        






