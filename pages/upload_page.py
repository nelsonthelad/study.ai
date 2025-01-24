import customtkinter as ctk
import os
from nlp_processing import generate_study_questions
import json
from save_processing import save_json_to_file

class QuestionsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, questions=None):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.output = questions if questions is not None else "No text available"

        data = json.loads(self.output)

        i = 0
        for question in data['questions']:
            question_label = ctk.CTkLabel(
                self,
                text=f"({i + 1}) {question['question']}",
                font=ctk.CTkFont(size=16),
                wraplength=400,
                justify="left"
            )
            question_label.grid(row=i, sticky="w", pady=15, padx=15)
            i += 1


class LoadingPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # setting up the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # loading label
        self.loading_label = ctk.CTkLabel(
            self,
            text="Loading...",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        self.loading_label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

class OutputFrame(ctk.CTkFrame):
    def __init__(self, master, output=None, go_main_menu_command=None):
        super().__init__(master)

        self.output = output if output is not None else "No text available"

        # setting up the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # output label
        self.output_label = ctk.CTkLabel(
            self,
            text="Generated Questions:",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.output_label.grid(row=0, column=0, pady=10, padx=10)

        self.preview_frame = QuestionsFrame(
            self,
            questions=self.output
        )
        self.preview_frame.grid(row=1, column=0, sticky="nsew", padx=15)

        # save button
        self.save_button = ctk.CTkButton(
            self, 
            text="Save", 
            command=lambda: self.save_question(self.output),
            text_color_disabled="dark_color"
        )
        self.save_button.grid(row=2, column=0, pady=15, padx=15)

    def save_question(self, text=None):
        dialog = ctk.CTkInputDialog(text="Enter filename to save as:", title="Save File")
        filename = dialog.get_input()

        if filename:
            self.save_button['state'] = 'disabled'
            try:
                save_json_to_file(text, filename)
                print(f"File saved as: {filename}")
            except Exception as e:
                print(f"Error saving file: {e}")
                self.save_button['state'] = 'normal'
        else:
            print("Save operation cancelled.")

        self.master.go_main_menu()
        

class PDFTextPreview(ctk.CTkFrame):
     def __init__(self, master, text=None, filepath=None):
        super().__init__(master)

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # external variables
        self.text = text if text is not None else "No text available"
        self.filepath = filepath if filepath is not None else "No file selected"

        # Get just the filename from the full path
        self.filename = os.path.basename(self.filepath) if self.filepath != "No file selected" else "No file selected"

        # preview label
        self.preview_label = ctk.CTkLabel(
            self,
            text=f"File: {self.filename}",
            font=ctk.CTkFont(size=12, weight="bold"),
            wraplength=400
        )
        self.preview_label.grid(row=0, column=0, pady=(20, 10), padx=15, sticky="nsew")

        # pulled text frame
        self.preview_text = ctk.CTkTextbox(
            self,
            corner_radius=10,
        )
        self.preview_text.grid(row=1, pady=20, padx=15, sticky="nsew")
        self.preview_text.insert("0.0", self.text)
        self.preview_text.configure(state="disabled")

        # generate button
        self.generate_button = ctk.CTkButton(
            self, 
            text="AI Generate", 
            command=lambda: master.gen_questions(self.text)
        )
        self.generate_button.grid(row=2, column=0, pady=15)


class UploadPage(ctk.CTkFrame):
    def __init__(self, master, text=None, filepath=None):
        super().__init__(master)

        # external variables
        self.text = text if text is not None else "No text available"
        self.filepath = filepath if filepath is not None else "No file selected"

        # grid system setup
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # header Label
        self.header_label = ctk.CTkLabel(
            self,
            text="Study.AI",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.header_label.grid(row=0, column=0, pady=20, padx=15, sticky="n")

        # menu button
        self.menu_button = ctk.CTkButton(
            self, 
            text="Menu", 
            command=self.go_main_menu
        )
        self.menu_button.grid(row=0, column=0, pady=15, padx=15, sticky="s")

        self.preview_frame = PDFTextPreview(self, text=self.text, filepath=self.filepath)
        self.preview_frame.grid(row=0, column=1, sticky="nsew")

    def go_main_menu(self):
        from .home_page import HomePage
        self.master.show_frame(HomePage)

    def gen_questions(self, text):
        print("Loading...")

        self.preview_frame.grid_forget()  
        self.loading_frame = LoadingPage(self)
        self.loading_frame.grid(row=0, column=1, sticky="nsew")

        self.after(100, lambda: self.process_questions(text))

    def process_questions(self, text):
        output = generate_study_questions(text)
        print(output)

        self.loading_frame.grid_forget()  # Hide the loading frame
        
        # Create a new text box to display the output
        self.output_frame = OutputFrame(self, output, go_main_menu_command=self.go_main_menu)
        self.output_frame.grid(row=0, column=1, sticky="nsew")