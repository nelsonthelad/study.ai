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
        if self.id + 1 < self.numquestions:  # Check if there are more questions
            self.id += 1
            self.question_frame.destroy()  # Properly destroy the old frame
            self.question_frame = QuestionFrame(self, id=self.id, data=self.data)
            self.question_frame.grid(row=0, column=0, stick="nsew")
    
    def check_answer(self):
        self.question_frame.check_answer()

    def quit(self):
        from .saved_page import SavedPage
        self.master.show_frame(SavedPage)


class QuestionFrame(ctk.CTkFrame):
    def __init__(self, master, id, data):
        super().__init__(master)
        
        self.data = data
        self.question_id = id
        self.checkboxes = []
        self.selected_answer = None
        self.answered = False  # Track if question has been answered

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

        result = "Correct!" if data['questions'][id]['answer'] == selected else "Incorrect!"
        
        for checkbox in self.checkboxes:
            checkbox.grid_forget()
    
        self.result_label = ctk.CTkLabel(
            self,
            text=result,
            font=ctk.CTkFont(size=42),
            fg_color="#3b3b3b",  
            corner_radius=8,           
            anchor="center",
        )
        self.result_label.grid(row=3, column=0, pady=100, padx=100, sticky="nsew")