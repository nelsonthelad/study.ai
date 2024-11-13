import PyPDF2
from fpdf import FPDF

def extract_text_from_pdf(file_path):
    error_message = "Error processing PDF to String"
    try:
        # Open the PDF file in binary mode
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file) # Create a PDF reader object
            num_pages = len(pdf_reader.pages) # Get total number of pages
            text = "" # Initialize string to store text
            
            # Extract text from each page
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num] # Get the page object
                text += page.extract_text() # Extract text from page
                
            return text
            
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return error_message

def gen_pdf_study_guide(text, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(40, 10, text)
    pdf.output(file_name)


    