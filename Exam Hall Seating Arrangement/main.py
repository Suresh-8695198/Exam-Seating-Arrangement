# main_program.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QFileDialog, QMessageBox
from design_module import DesignModule
from allocation_module import AllocationModule
from pdf_module import PdfModule

class MainProgram(QWidget):
    def __init__(self):
        super().__init__()

        self.design_module = DesignModule(self)
        self.allocation_module = AllocationModule(self)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Classroom Generator')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        layout.addWidget(self.design_module)
        self.generate_excel_button = QPushButton('Generate Excel Output', self)
        self.generate_excel_button.clicked.connect(self.generate_excel_output)
        layout.addWidget(self.generate_excel_button)

        self.generate_pdf_button = QPushButton('Generate PDF Output', self)
        self.generate_pdf_button.clicked.connect(self.generate_pdf_output)
        layout.addWidget(self.generate_pdf_button)

        self.setLayout(layout)

    def generate_excel_output(self):
        file_path = self.design_module.file_entry.text()
        students_per_class = int(self.design_module.class_entry.text())
        rows = int(self.design_module.rows_entry.text())
        columns = int(self.design_module.columns_entry.text())

        l3, _ = self.allocation_module.read_excel_and_generate_output(file_path, students_per_class)
        self.allocation_module.generate_excel_output(l3, students_per_class, rows, columns)

    def generate_pdf_output(self):
        file_path = self.design_module.file_entry.text()
        students_per_class = int(self.design_module.class_entry.text())
        rows = int(self.design_module.rows_entry.text())
        columns = int(self.design_module.columns_entry.text())

        l3, _ = self.allocation_module.read_excel_and_generate_output(file_path, students_per_class)

        pdf = PdfModule.generate_pdf_output(l3, students_per_class, rows, columns)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF file", "AllocatedStudents.pdf", "PDF Files (*.pdf);;All Files (*)", options=options)

        if filename:
            pdf.output(filename)
            QMessageBox.information(self, 'Success', f'PDF file "{filename}" has been created successfully.')

def main():
    app = QApplication(sys.argv)
    window = MainProgram()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
