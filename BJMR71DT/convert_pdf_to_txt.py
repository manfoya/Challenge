
import PyPDF2
import os

def convert_pdf_to_txt(pdf_path, txt_path):
    """
    Extrait le texte d'un fichier PDF et le sauvegarde dans un fichier texte.

    Args:
        pdf_path (str): Le chemin vers le fichier PDF d'entrée.
        txt_path (str): Le chemin vers le fichier texte de sortie.
    """
    if not os.path.exists(pdf_path):
        print(f"Erreur : Le fichier PDF '{pdf_path}' n'a pas été trouvé.")
        return

    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
        
        print(f"Conversion réussie ! Le texte a été sauvegardé dans '{txt_path}'")

    except Exception as e:
        print(f"Une erreur est survenue lors de la conversion : {e}")

if __name__ == '__main__':
    # Nom du fichier PDF à convertir (assurez-vous qu'il est dans le même dossier)
    pdf_filename = 'Instructions.pdf'
    
    # Nom du fichier texte de sortie
    txt_filename = 'instructions.txt'

    # Obtenir le chemin absolu du répertoire du script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construire les chemins complets pour les fichiers
    pdf_input_path = os.path.join(script_dir, pdf_filename)
    txt_output_path = os.path.join(script_dir, txt_filename)

    # Lancer la conversion
    convert_pdf_to_txt(pdf_input_path, txt_output_path)
