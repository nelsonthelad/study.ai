import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import customtkinter as ctk
from pages.home_page import HomePage

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("study.ai")
        self.geometry("720x480")
        ctk.set_appearance_mode("Dark")  
        ctk.set_default_color_theme("blue")
        
        self.current_frame = None
        self.show_frame(HomePage)

    def show_frame(self, page_class, *args, **kwargs):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = page_class(self, *args, **kwargs)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()



