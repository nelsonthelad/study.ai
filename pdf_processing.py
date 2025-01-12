import PyPDF2

def extract_text_from_pdf(file_path):
    error_message = "Error processing PDF to String"
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file) 
            num_pages = len(pdf_reader.pages) # 
            text = "" 
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num] 
                text += page.extract_text() 
                
            return text
            
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return error_message


    