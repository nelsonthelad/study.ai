import customtkinter as ctk
from tkinter import filedialog
from pdf_processing import extract_text_from_pdf


class UploadPage(ctk.CTkFrame):
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
        
        #upload button 
        self.upload_button = ctk.CTkButton(
            self, 
            text="Upload PDF",
            command=self.upload_pdf,
            width=200,
            height=40
        )
        self.upload_button.grid(row=1, column=0, pady=30)

        # back button
        self.back_button = ctk.CTkButton(
            self,
            text="Menu",
            command=self.go_main_menu,
            width=200,
            height=40
        )
        self.back_button.grid(row=2, column=0, pady=30)

        # footer
        self.footer_label = ctk.CTkLabel(
            self,
            text="Developed by Nelson Daniels V1.1",
            font=ctk.CTkFont(size=8)
        )
        self.footer_label.grid(row=3, column=0, pady=10)

    def go_main_menu(self):
        from .home_page import HomePage
        self.master.show_frame(HomePage)

    def upload_pdf(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Select PDF",
                filetypes=[("PDF files", "*.pdf")],
                parent=self
            )
            if file_path:
                # Hide buttons
                self.upload_button.grid_forget()
                #self.back_button.grid_forget()

                # loading text
                self.status_label = ctk.CTkLabel(
                    self,
                    text="loading...",
                    font=ctk.CTkFont(size=16, weight="bold")
                )
                self.status_label.grid(row=1, column=0, pady=30)

                # Process the PDF
                text = extract_text_from_pdf(file_path)
                print(text)

                # Stop loading bar and show buttons again
                #self.loading_label.grid_forget()
                #self.upload_button.grid(row=1, column=0, pady=30)
                #self.back_button.grid(row=2, column=0, pady=30)
        except Exception as e:
            print(f"Error during file selection: {e}")