import os
import nbformat
import subprocess
from nbformat.v4 import new_notebook , new_code_cell

directory = os.path.join(os.getcwd())

def create_project_structure():

    directory = os.path.join(os.getcwd())
    folders = ["data/raw", "data/cleaned", "docs",
               "models", "notebooks", "reports", "src"]


    for folder in folders:
            
            folder_path = os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)
            # Crée un fichier .gitkeep dans les dossiers vides pour qu'ils soient suivis
            with open(os.path.join(folder_path, ".gitkeep"), 'w') as f:
                pass

def create_initial_files():

    files = ["LICENSE", "Makefile", "README.md", ".gitignore",
             "requirements.txt"]

    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            file_content = ''
            f.write(file_content)


def add_specific_files():

    # verifiez si les dossiers existe deja 
    os.makedirs('notebooks', exist_ok=True)
    # Ajoutez une cellule de code au notebook et remplissage du fichier mains.ipynb du notebook
    notebook = new_notebook()
    code_source = "print('Hello, world!')"
    cell = new_code_cell(source=code_source)
    notebook.cells.append(cell)
    main_notebook_path = os.path.join(directory, "notebooks/main.ipynb")
    if not os.path.exists(main_notebook_path):
    
        with open(main_notebook_path, "w") as main_notebook_file:
            nbformat.write(notebook,main_notebook_file)
    # ajout du fichier utils.py
    os.makedirs(os.path.join(directory, "src/utils.py"), exist_ok=True)


def main():
   
    create_project_structure()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Ajout de la structure de base du projet closes #1"])

    create_initial_files()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Ajout des fichiers initiaux .closes #2"])

    add_specific_files()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Ajout des fichiers spécifiques closes #3"])
main()