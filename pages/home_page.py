import customtkinter as ctk
from .upload_page import UploadPage
from .saved_page import SavedPage
from tkinter import filedialog
from pdf_processing import extract_text_from_pdf

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # grid system setup
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 3), weight=1)

        # header
        self.header_label = ctk.CTkLabel(
            self,
            text="study.ai",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        self.header_label.grid(row=0, column=0, pady=20)
        
        # upload button
        self.upload_button = ctk.CTkButton(
            self, 
            text="Upload", 
            width=300, 
            height=70,
            command=self.upload_handle
        )
        self.upload_button.grid(row=1, column=0, pady=15)

        # saved button
        self.saved_button = ctk.CTkButton(
            self,
            text="Saved",
            width=300,
            height=70,
            command=self.go_to_saved_page
        )
        self.saved_button.grid(row=2, column=0, pady=15)

        # footer
        self.footer_label = ctk.CTkLabel(
            self,
            text="Developed by Nelson Daniels V1.1",
            font=ctk.CTkFont(size=8)
        )
        self.footer_label.grid(row=3, column=0, pady=10)
        
    #logic for upload button
    def upload_handle(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Select PDF",
                filetypes=[("PDF files", "*.pdf")],
                parent=self
            )
            if file_path:
                # Process the PDF
                text = extract_text_from_pdf(file_path)
                self.master.show_frame(UploadPage, text=text, filepath=file_path)

        except Exception as e:
            print(f"Error during file selection: {e}")

    def go_to_saved_page(self):
        self.master.show_frame(SavedPage)