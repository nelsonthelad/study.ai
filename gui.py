from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget

class StudyToolGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("AI Study Tool")
        self.setGeometry(100, 100, 400, 200)
        
        # Layout setup
        layout = QVBoxLayout()

        # Label to show status messages
        self.status_label = QLabel("Select a PDF to begin.", self)
        layout.addWidget(self.status_label)

        # Button to open PDF
        open_button = QPushButton('Open PDF', self)
        open_button.clicked.connect(self.open_pdf_dialog)
        layout.addWidget(open_button)

        # Set the central widget and layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_pdf_dialog(self):
        # Open file dialog to select a PDF
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if file_path:
            self.status_label.setText(f"Selected file: {file_path}")
            self.process_pdf_stub(file_path)

    def process_pdf_stub(self, file_path):
        # This is a placeholder for actual processing logic
        # For now, it just updates the status label to indicate that processing is "complete"
        self.status_label.setText(f"Processing complete! (Stub) File: {file_path}")

# This is just the GUI file; main.py will launch the interface.
