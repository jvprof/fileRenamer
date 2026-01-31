# prends tous les sous dossier d'un dossier et les renomme en inversant le no et le prenom
import os
from src.logger import get_logger

logger = get_logger('renamer')


class Renamer:

    def name_surname_inverter(self, directory, sep=" "):
        """ Renomme les sous-dossiers dans le répertoire donné en inversant
            le nom et le prénom séparés par `sep`.
        """
        for root, dirs, files in os.walk(directory):
            logger.debug("Processing directory: %s", root)
            for name in dirs:
                logger.info("Found directory: %s", name)
                if sep in name:
                    prenom = name.split(sep)[0]
                    nom = name[name.find(sep)+1:]
                    logger.debug("Extracted nom: %s, prenom: %s", nom, prenom)
                    new_name = f"{nom} {prenom}"
                    logger.info("Renaming: %s -> %s", name, new_name)
                    logger.debug("Old path: %s", os.path.join(root, name))
                    logger.debug("New path: %s", os.path.join(root, new_name))
                    os.rename(os.path.join(root, name), os.path.join(root, new_name))



