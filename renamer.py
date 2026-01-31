# prends tous les sous dossier d'un dossier et les renomme en inversant le no et le prenom
import os
from PySide6.QtWidgets import QApplication, QFileDialog
import sys
def rename_dirs_in_directory(directory, sep=" "):
    for root, dirs, files in os.walk(directory):
        # print(f"Processing directory: {root}")
        for name in dirs:
            print(f"Found directory: {name}")
            if sep in name:
                prenom = name.split(sep)[0]
                nom = name[name.find(sep)+1:]
                print(f"Extracted nom: {nom}, prenom: {prenom}")
                new_name = f"{nom} {prenom}"
                print(f"Renaming: {name} -> {new_name}")
                print(f"Old path: {os.path.join(root, name)}")
                print(f"New path: {os.path.join(root, new_name)}")
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
# Exemple d'utilisation
# rename_dirs_in_directory('/chemin/vers/le/dossier')



app = QApplication(sys.argv)
userHomeDir = os.path.expanduser("~")
# dir = QFileDialog.getExistingDirectory(None, "Sélectionnez un dossier", userHomeDir)
dir= "/Users/jonathan.vasseur/Library/CloudStorage/OneDrive-EducationVaud/2526/TEST_OD/1M7/TEST-ARCHITECTURE-1M7_-_2026"
if dir:
    print(f"Dossier sélectionné : {dir}")
    rename_dirs_in_directory(dir)
else:
    print("Aucun dossier sélectionné.")
    # Pour tester sans interface graphique, décommentez la ligne suivante et spécifiez un chemin
    # dir = '/chemin/vers/le/dossier'

rename_dirs_in_directory(dir)
