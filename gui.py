from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

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
        print("Processing PDF...")

        # Update the status label and hide the button
        self.status_label.setText("Processing PDF...")
        self.open_button.hide()
        # This is a placeholder for actual processing logic
        # For now, it just updates the status label to indicate that processing is "complete"
        # self.status_label.setText(f"Processing complete! (Stub) File: {file_path}")