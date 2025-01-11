import customtkinter as ctk

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # grid system setup
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 3), weight=1)
        
        # header
        self.header_label = ctk.CTkLabel(self, text="study.ai", font=ctk.CTkFont(size=32, weight="bold"))
        self.header_label.grid(row=0, column=0, pady=20)
        
        # upload button
        self.upload_button = ctk.CTkButton(self, text="Upload New Study Material", width=300, height=70)
        self.upload_button.grid(row=1, column=0, pady=15)

        # saved button
        self.saved_button = ctk.CTkButton(self, text="Saved Practice Problems", width=300, height=70)
        self.saved_button.grid(row=2, column=0, pady=15)

        # footer
        self.footer_label = ctk.CTkLabel(self, text="Developed by Nelson Daniels V1.1", font=ctk.CTkFont(size=8))
        self.footer_label.grid(row=3, column=0, pady=10)
        

    def on_button_click(self):
        ctk.CTkMessagebox.show_info(title="Button Clicked", message="Hello from the Home Page!")
