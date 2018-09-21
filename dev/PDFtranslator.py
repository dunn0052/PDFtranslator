#pdf translator

from googletrans import Translator
import crw
import PyPDF2
import re
import os

directory_path = os.path.dirname(os.path.realpath(__file__))
pdf_path = "\\to_be_translated\\"
finished_path = "\\translation_results\\"
PDF_list = os.listdir(directory_path + pdf_path)
file_type = "(.*).pdf"
translator = Translator()

def lineSplit(text, max_line = 80):
    text_length = len(text)
    lines = []
    index = -1
    lindex = max_line
    while lindex < text_length -1:
        while text[lindex] != " ":
            lindex -= 1
        lines.append(text[index+1:lindex] + "\n")
        index = lindex
        lindex += max_line
    if index < text_length:
        lines.append(text[index+1:text_length] + "\n")
    return lines


for pdf in PDF_list:
    capture = re.compile(file_type)
    s = capture.findall(pdf)
    if s != []:
        pages = []
        translated = []
        PDF = open(directory_path + pdf_path + pdf, "rb")
        reader = PyPDF2.PdfFileReader(PDF)
        print("Opened", s[0])
        for page_num in range(reader.getNumPages()):
            pages.append(reader.getPage(page_num))
            t = translator.translate(pages[page_num].extractText())
            translated.append(lineSplit(t.text))
        print("Translated", s[0])
        save_file = open(directory_path + finished_path + s[0] + "_translated.txt", "w")
        for page in translated:
            save_file.writelines(page)
        save_file.close()
        print("Saved", save_file.name)
        PDF.close()


    
    

