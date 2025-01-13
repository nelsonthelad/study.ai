import customtkinter as ctk
import os


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

    