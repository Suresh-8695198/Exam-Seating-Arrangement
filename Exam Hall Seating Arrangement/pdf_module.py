# pdf_module.py
from fpdf import FPDF
from PyQt5.QtWidgets import QMessageBox, QFileDialog
class PdfModule:
    @staticmethod
    def generate_pdf_output(l3, students_per_class, rows, columns):
        class CustomPDF(FPDF):
            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", style='I', size=8)
                self.set_text_color(128, 128, 128)  # Gray color
                self.cell(0, 10, "Developed by @Suresh G", 0, 0, 'C')
        if rows * columns < students_per_class or rows * columns > students_per_class:
            QMessageBox.critical(None, 'Error', 'The specified number of rows and columns is not sufficient to accommodate the students per class.')
            return  # Return None as an indication of error

        pdf = CustomPDF()  
        pdf.set_auto_page_break(auto=True, margin=15)  
        pdf.set_font("Arial", size=7)  

        students_total = len(l3)
        classes = -(-students_total // students_per_class)

        for i in range(classes):
            start_row = i * students_per_class
            end_row = min((i + 1) * students_per_class, students_total)
            class_data = l3[start_row:end_row]

            pdf.add_page()
            # Calculate the x-coordinate to center the table horizontally
            x_center = (pdf.w - 190) / 2  # 190 is the total width of the table
            
            # Add Title: VYSYA COLLEGE
            pdf.set_font("Arial", style='B', size=24)  # Large and bold font for the title
            pdf.cell(200, 10, txt='VYSYA COLLEGE', ln=True, align='C')  
            pdf.set_font("Arial", size=7)  # Reset font style to normal

            # Add Title: Exam HALL Seating Arrangement
            pdf.set_font("Arial", style='B', size=18)  # Large and bold font for the title
            pdf.cell(200, 10, txt='EXAM HALL SEATING ARRANGEMENT', ln=True, align='C')  
            pdf.set_font("Arial", size=7)  # Reset font style to normal

            
            
            # Add ROOM Title
            pdf.set_font("Arial", style='B', size=10)  # Bold and larger font for room title
            room_title = f'ROOM {i + 1}'
            room_title_width = pdf.get_string_width(room_title)
            x_center = (pdf.w - 190) / 2  # Adjust x-coordinate for perfect centering
            pdf.cell(200, 10, txt=room_title, ln=True, align='C')
            pdf.set_font("Arial", size=7)  # Reset font style to normal

            total_tables = -(-len(class_data) // (rows * columns))

            for table_index in range(total_tables):
                pdf.ln()  
                 

                # Add column headers with bold font
                pdf.set_x(x_center)
                pdf.set_font("Arial", style='B', size=7)  # Bold font
                for col_header in range(1, columns + 1):
                    pdf.cell(190 / columns, 10, txt=f'Column {col_header}', border=1, ln=0, align='C')
                pdf.set_font("Arial", size=7)  # Reset font style to normal
                pdf.ln()
                
                cell_height = 15
                cell_width = 190 / columns  # Corrected cell width calculation
                
                # Move to the center of the page before drawing the table
                pdf.set_x(x_center)
                
                for row in range(rows):  # Iterate over rows first
                    pdf.ln()
                    for col in range(columns):  # Then iterate over columns
                        index = table_index * (rows * columns) + row + col * rows  # Swap row and col
                        if index < len(class_data):
                            student_id = class_data[index]
                            pdf.cell(cell_width, cell_height, student_id, 1, 0, 'C')
                        else:
                            pdf.cell(cell_width, cell_height, '', 1, 0, 'C')  

                pdf.ln()  

        return pdf
