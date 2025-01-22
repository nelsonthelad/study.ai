import customtkinter as ctk
import json

class StudyPage(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        self.id = 0

        self.data = data
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
            text="Submit"
        )
        self.submit_button.grid(row=1, column=0, padx=15, pady=15, sticky="w")

    def get_num_questions(self, data=None):
        if data is None:
            print("No Data")
            return None
        
        if isinstance(data, str):
            data = json.loads(data)
        
        return len(data['questions'])


class QuestionFrame(ctk.CTkFrame):
    def __init__(self, master, id, data):
        super().__init__(master)
        
        self.data = data
        self.question_id = id

        self.question = self.get_question(self.data, self.question_id)

        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.question_label = ctk.CTkLabel(
            self,
            text=self.question,
            font=ctk.CTkFont(size=20),
            wraplength=450
        )
        self.question_label.grid(row=0, column=0, stick="n", pady=20)

        self.answers = self.get_answers(self.data, self.question_id)

        for i in range(len(self.answers)):
            checkbox = ctk.CTkCheckBox(
                self,
                text=self.answers[i],
                font=ctk.CTkFont(size=32)
            )
            checkbox.grid(row=i+1, column=0, padx=40, pady=(10, 0), sticky="w")

    def get_question(self, data, id):
        if data is None or 'questions' not in data:
            return None
        
        return data['questions'][id]['question']
        

    def get_answers(self, data, id):
        return data['questions'][id]['options']
