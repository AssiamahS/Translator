import PyPDF2
from googletrans import Translator

def translate_pdf(input_pdf, output_pdf, dest_lang):
    # Initialize PDF reader and writer
    pdf_reader = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
    pdf_writer = PyPDF2.PdfFileWriter()
    
    # Initialize Google Translator
    translator = Translator()
    
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        
        # Translate text
        translated_text = translator.translate(text, dest=dest_lang).text
        
        # Create a new PDF with the translated text
        translated_page = pdf_writer.addBlankPage(
            width=page.mediaBox.getWidth(), 
            height=page.mediaBox.getHeight()
        )
        
        translated_page.insertText(translated_text)
    
    with open(output_pdf, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

input_pdf = 'input.pdf'  # PDF to translate
output_pdf = 'translated_output.pdf'  # Translated PDF
dest_lang = 'es'  # Target language, e.g., 'es' for Spanish, 'en' for English

translate_pdf(input_pdf, output_pdf, dest_lang)
