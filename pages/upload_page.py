import customtkinter as ctk

class UploadPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # grid system setup
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 2), weight=1)
        
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
        self.upload_button.grid(row=1, column=0, pady=20)

        # footer
        self.footer_label = ctk.CTkLabel(
            self,
            text="Developed by Nelson Daniels V1.1",
            font=ctk.CTkFont(size=8)
        )
        self.footer_label.grid(row=2, column=0, pady=10)

    def upload_pdf(self):
        file_path = ctk.filedialog.askopenfilename(
            title="Select PDF",
            filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            print(f"Selected file: {file_path}")