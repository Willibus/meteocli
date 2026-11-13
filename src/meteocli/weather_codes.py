"""Conversion des codes météo WMO en texte lisible."""

WMO_CODES = {
    0: "Ciel dégagé",
    1: "Plutôt dégagé",
    2: "Partiellement nuageux",
    3: "Couvert",
    45: "Brouillard",
    48: "Brouillard givrant",
    51: "Bruine légère",
    53: "Bruine",
    55: "Bruine forte",
    61: "Pluie légère",
    63: "Pluie",
    65: "Pluie forte",
    71: "Neige légère",
    73: "Neige",
    75: "Neige forte",
    80: "Averses légères",
    81: "Averses",
    82: "Averses violentes",
    95: "Orage",
    96: "Orage avec grêle",
    99: "Orage violent avec grêle",
}


def describe_code(code: int) -> str:
    return WMO_CODES.get(code, "Inconnu")