from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtCore import Qt
from pdf_processing import extract_text_from_pdf

class StudyToolGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("study.ai")
        self.setGeometry(100, 100, 400, 200)
        
        # Layout setup
        layout = QVBoxLayout()

        # Label to show status messages
        self.status_label = QLabel("Select a PDF to begin.", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Button to open PDF
        self.open_button = QPushButton('Open PDF', self)
        self.open_button.clicked.connect(self.open_pdf_dialog)
        layout.addWidget(self.open_button)

        # Set the central widget and layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def pdf_to_string(self, text):
        # Create a new window to display the text
        text_window = QMainWindow()
        text_window.setWindowTitle("PDF Content")
        text_window.setGeometry(200, 200, 600, 400)

        # Create a label to display the text
        text_label = QLabel(text)
        text_label.setWordWrap(True)
        text_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Make the text selectable
        text_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Create a scroll area to handle long text
        scroll_area = QScrollArea()
        scroll_area.setWidget(text_label)
        scroll_area.setWidgetResizable(True)

        # Set the scroll area as the central widget
        text_window.setCentralWidget(scroll_area)
        text_window.show()


    def open_pdf_dialog(self):
        # Open file dialog to select a PDF
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if file_path:
            file_name = file_path.split('/')[-1]  # Extract the file name from the full path
            self.status_label.setText(f"Selected file: {file_name}")

            # Update What the button does
            self.open_button.setText("Generate Study Guide")
            self.open_button.clicked.disconnect() 
            self.open_button.clicked.connect(lambda: self.process_pdf_stub(file_path))

    def process_pdf_stub(self, file_path):
        error_message = "Error processing PDF to String"
        print("Processing PDF...")

        # Update the status label and hide the button
        self.status_label.setText("Processing PDF...")
        self.open_button.hide()

        # Extract text from the PDF
        print("Starting extraction...")
        text = extract_text_from_pdf(file_path)
        print("Extraction complete.")
        if text == error_message:
            self.status_label.setText("Error processing PDF to String")
        else:
            print(text)
            self.pdf_to_string(text) # Display the text in a new window for testing purposes

        

