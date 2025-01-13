import customtkinter as ctk

class SavedFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.saved_data = []
        
        # Initialize the checkboxes list
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(
                self,
                text=value,
                command=lambda i=i: self.select_checkbox(i)  # Pass the index instead
            )
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def select_checkbox(self, selected_index):
        # Deselect all checkboxes except the selected one
        for i, checkbox in enumerate(self.checkboxes):
            if i != selected_index:
                checkbox.deselect()
            else:
                checkbox.select()


class PreviewFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #grid setup
        self.grid_rowconfigure(1, weight=1)

        #labels
        self.preview_label = ctk.CTkLabel(
            self,
            text="Preview",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.preview_label.grid(row=0, column=0, pady=10, padx=15)

        self.score_label = ctk.CTkLabel(
            self,
            text="Score",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.score_label.grid(row=0, column=1, pady=10, padx=15)

        #preview and score
        self.preview_text = ctk.CTkTextbox(
            self,
            corner_radius=10,
        )
        self.preview_text.grid(row=1, column=0, pady=20, padx=15, sticky="ns")
        self.preview_text.insert("0.0", "Coming soon...")

        self.score_text = ctk.CTkTextbox(
            self,
            corner_radius=10,
        )
        self.score_text.grid(row=1, column=1, pady=20, padx=15, sticky="ns")
        self.score_text.insert("0.0", "Coming soon...")
        

class SavedPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # grid system setup
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #area to store the items
        values = ["Saved 1", "Saved 2", "Saved 3", "Saved 4", "Saved 5", 
                 "Saved 6", "Saved 7", "Saved 8", "Saved 9", "Saved 10"]
        
        self.saved_scroll_frame = SavedFrame(self, title="Saved", values=values)
        self.saved_scroll_frame.grid(row=0, column=0, sticky="nsew")

        self.preview_frame = PreviewFrame(self)
        self.preview_frame.grid(row=0, column=1, sticky="nsew")

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
            text="Practice"
        )
        self.practice_button.grid(row=1, column=1, pady=15)

    def go_main_menu(self):
        from .home_page import HomePage
        self.master.show_frame(HomePage)