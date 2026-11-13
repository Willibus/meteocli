# meteocli

CLI Python qui affiche la météo actuelle et les prévisions d'une ville
grâce à l'API publique [Open-Meteo](https://open-meteo.com/) (sans clé API).

## Prérequis
- Python >= 3.10
- [Poetry](https://python-poetry.org/docs/) >= 2.0
- Une connexion internet

## Installation
```bash
git clone https://github.com/Willibus/meteocli.git
cd meteocli
poetry install
```

## Utilisation
exemples d'utilisation 
```bash
poetry run meteocli Lyon --days 3
poetry run meteocli --help
```

## Tests et qualité
```bash
poetry run pytest
poetry run ruff check .
```

## Build et packaging
```bash
poetry build        # génère dist/*.whl et dist/*.tar.gz
```
Installer la wheel produite : `pip install dist/meteocli-0.2.0-py3-none-any.whl`

## Usage de l'outil de build (Poetry)
| Tâche | Commande |
|---|---|
| Gestion des dépendances | `poetry add <pkg>`, `poetry add --group dev <pkg>`, `poetry lock` (fichier `poetry.lock` versionné) |
| Compilation | `python -m compileall src` ; la wheel est produite par `poetry build` |
| Gestion des versions | `poetry version patch\|minor\|major` puis `git tag vX.Y.Z` |
| Packaging | `poetry build` (wheel + sdist dans `dist/`) |

## Structure
```
meteocli/
├── src/meteocli/
│   ├── api.py            
│   ├── models.py         
│   ├── weather_codes.py  # codes WMO -> texte
│   └── cli.py            
├── tests/
│   └── test_meteocli.py  
├── pyproject.toml        # métadonnées, dépendances, scripts
├── poetry.lock           
├── .gitignore
└── README.md
```


## Licence
MIT