
import docx
import os

def convert_docx_to_txt(docx_path, txt_path):
    try:
        document = docx.Document(docx_path)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for para in document.paragraphs:
                txt_file.write(para.text + '\n')
        print(f"Successfully converted {docx_path} to {txt_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    docx_file = '/home/_mars/DataAxard/BASE 2 (EDS)/EDS2017-2018/Canevas_Rapport_Concours.docx'
    txt_file = '/home/_mars/DataAxard/BASE 2 (EDS)/EDS2017-2018/Canevas_Rapport_Concours.txt'
    
    if os.path.exists(docx_file):
        convert_docx_to_txt(docx_file, txt_file)
    else:
        print(f"The file {docx_file} does not exist.")
