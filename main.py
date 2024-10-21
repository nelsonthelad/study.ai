import sys
from PyQt5.QtWidgets import QApplication
from gui import StudyToolGUI

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create the GUI window
    window = StudyToolGUI()
    window.show()

    # Execute the application
    sys.exit(app.exec_())
