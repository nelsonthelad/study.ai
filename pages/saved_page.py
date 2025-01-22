import customtkinter as ctk
import os
import json

class SavedFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values, info_frame):
        super().__init__(master, label_text=title, scrollbar_button_color="#333333", scrollbar_button_hover_color="#333333")
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.saved_data = []
        self.info_frame = info_frame
        self.selected_file = None
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(
                self,
                text=value,
                command=lambda i=i: self.select_checkbox(i) 
            )
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def select_checkbox(self, selected_index):
        for i, checkbox in enumerate(self.checkboxes):
            if i != selected_index:
                checkbox.deselect()
            else:
                checkbox.select()
                filename = self.values[selected_index]
                data = self.get_file_data(filename)
                self.selected_file = data
                self.info_frame.UpdateInfo(data)

    def get_file_data(self, file=None):
        if file is None:
            return None
        
        file_path = os.path.join("saved", f"{file}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return None
    
    def return_selected_file(self):
        return self.selected_file


class InfoFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, label_text="Info", scrollbar_button_color="#333333", scrollbar_button_hover_color="#333333")

        #grid setup
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #labels
        self.creation_label = ctk.CTkLabel(
            self,
            text="Date Created: ",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.creation_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.questions_num_label = ctk.CTkLabel(
            self,
            text="Number of Questions:",
            font=ctk.CTkFont(size=12, weight="bold")

        )
        self.questions_num_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.score_label = ctk.CTkLabel(
            self,
            text="Score: ",
            font=ctk.CTkFont(size=12, weight="bold")

        )
        self.score_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        self.questions_label = ctk.CTkLabel(
            self,
            text="Questions",
            fg_color="#3b3b3b",  
            corner_radius=8,
            width=130,              
            height=30,           
            anchor="center", 
        )
        self.questions_label.grid(row=3, column=0, stick="ew")

    def UpdateInfo(self, data=None):
        if data:
            self.data = data
            
            self.creation_label.configure(text=f"Date Created: {data.get('metadata', {}).get('generated_on', 'N/A')}")
            self.questions_num_label.configure(text=f"Number of Questions: {data.get('metadata', {}).get('total_questions', 'N/A')}")
            self.score_label.configure(text=f"Score: {data.get('score', 'N/A')}")

            i = 0
            for question in data['questions']:
                question_label = ctk.CTkLabel(
                    self,
                    text=f"({i + 1}) {question['question']}",
                    font=ctk.CTkFont(size=12),
                    wraplength=350,
                    justify="left",
                )
                question_label.grid(row=i+4, sticky="nw", pady=15, padx=15)
                i += 1

class SavedPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # grid system setup
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create InfoFrame first
        self.info_frame = InfoFrame(self)
        self.info_frame.grid(row=0, column=1, sticky="nsew", padx=(15,0))
        
        # Then create SavedFrame with info_frame reference
        values = self.get_saved_files()
        self.saved_scroll_frame = SavedFrame(self, title="Saved", values=values, info_frame=self.info_frame)
        self.saved_scroll_frame.grid(row=0, column=0, sticky="nsew")

        # back button
        self.back_button = ctk.CTkButton(
            self,
            text="Menu",
            command=self.go_main_menu,
        )
        self.back_button.grid(row=1, column=0, pady=15)

        # practice button
        self.practice_button = ctk.CTkButton(
            self,
            text="Practice",
            command=self.go_study_page
        )
        self.practice_button.grid(row=1, column=1, pady=15)

    def go_main_menu(self):
        from .home_page import HomePage
        self.master.show_frame(HomePage)

    def get_saved_files(self):
        directory = "saved"

        files = [os.path.splitext(file)[0] for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

        return files
    
    def get_file_data(self, file=None):
        if file is None:
            return None
        
        file_path = os.path.join("saved", f"{file}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return None
        
    def go_study_page(self):
        data = self.saved_scroll_frame.return_selected_file()

        print(data)

        from .study_page import StudyPage
        self.master.show_frame(StudyPage, data)




       