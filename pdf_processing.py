import PyPDF2

def extract_text_from_pdf(file_path):
    error_message = "Error processing PDF to String"
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            text = ""
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                # Join lines and replace multiple spaces with single space
                page_text = page.extract_text()
                page_text = ' '.join(page_text.split())
                text += page_text + ' '
                
            return text.strip()
            
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return error_message


    