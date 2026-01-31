import os
import sys
# Ajouter la racine du projet au PATH afin que `import src...` fonctionne
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.core.renamer import Renamer
from PySide6.QtWidgets import QApplication, QFileDialog
from src.logger import get_logger

logger = get_logger('controller')

app = QApplication(sys.argv)
userHomeDir = os.path.expanduser("~")
renamer = Renamer()
# dir = QFileDialog.getExistingDirectory(None, "Sélectionnez un dossier", userHomeDir)
dir= "/Users/jonathan.vasseur/Library/CloudStorage/OneDrive-EducationVaud/2526/TEST_OD/1M7/TEST-ARCHITECTURE-1M7_-_2026"
if dir:
    logger.info("Dossier sélectionné : %s", dir)
    renamer.name_surname_inverter(dir)
else:
    logger.warning("Aucun dossier sélectionné.")
    sys.exit()
