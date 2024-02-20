# design_module.py
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog

class DesignModule(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.file_label = QLabel('Select Excel file:')
        self.file_entry = QLineEdit()
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_file)

        self.class_label = QLabel('Students per Class:')
        self.class_entry = QLineEdit()

        self.rows_label = QLabel('Rows:')
        self.rows_entry = QLineEdit()

        self.columns_label = QLabel('Columns:')
        self.columns_entry = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_entry)
        layout.addWidget(self.browse_button)

        layout.addWidget(self.class_label)
        layout.addWidget(self.class_entry)

        layout.addWidget(self.rows_label)
        layout.addWidget(self.rows_entry)

        layout.addWidget(self.columns_label)
        layout.addWidget(self.columns_entry)

        self.setLayout(layout)

    def browse_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Excel file', '/', 'Excel files (*.xlsx);;All files (*.*)')
        self.file_entry.setText(filename)
