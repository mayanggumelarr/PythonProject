from fpdf import FPDF                                                       # Import lib. fpd 
from docx import Document                                                   # Import lib. docx
import io                                                                   # Import lib. io -> open file

def convert_to_pdf(input_file, pdf_file) :                                  # Func. convert -> PDF
    with open(input_file, "r") as file:                                     # Open file awal
        content = file.read()                                               # Var. content = read file

    pdf = FPDF()                                                            # Var. pdf = class FPDF
    pdf.add_page()                                                          # make  new blank page 
    pdf.set_font("Arial", size=12)                                          # set font

    pdf.multi_cell(0, 10, content)                                          # multi_cell agar text otomatis terbungkus
    pdf.output(pdf_file)                                                    # save PDF

def convert_to_docx(input_file, docx_file)  :                               # Func. convert -> .docx
    with open(input_file, "r") as file:                                     # Open file awal
        content = file.read()                                               # Var. content = read file

    doc = Document()                                                        # make object dokumen word
    doc.add_paragraph(content)                                              # add text from context to new text docx
    doc.save(docx_file)                                                     # saving to .docx

convert_to_docx("C:\PYTHON\Project\ConvertFile\SKZ_Birthday.txt",           # implementation .docx
            "C:\PYTHON\Project\ConvertFile\SKZ_Birthday.docx")

convert_to_pdf("C:\PYTHON\Project\ConvertFile\SKZ_Birthday.txt",            # implementation .pdf
            "C:\PYTHON\Project\ConvertFile\SKZ_Birthday.pdf") 

          