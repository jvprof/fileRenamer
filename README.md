Renamer — instructions d'utilisation

Ce dépôt contient le script `renamer.py`.

Environnement virtuel

Un environnement virtuel local nommé `.venv` peut être utilisé. Pour créer/mettre à jour :

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
```

Activation (macOS / Linux) :

```bash
source .venv/bin/activate
```

Installer les dépendances (si un fichier `requirements.txt` existe) :

```bash
.venv/bin/python -m pip install -r requirements.txt
```

Lancer le script :

```bash
.venv/bin/python renamer.py
```

Remarques

- Si vous préférez, vous pouvez utiliser directement `.venv/bin/python` sans activer le venv.
- Fichier principal : `renamer.py`
