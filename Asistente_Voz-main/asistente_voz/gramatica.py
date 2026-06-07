"""
Gramática simplificada para validar comandos
"""

from asistente_voz.config import VERBOS, WAKE_WORDS

def comando_valido_según_gramatica(tokens: list[str]) -> bool:
    if not tokens or tokens[0] not in WAKE_WORDS:
        return False
    # Verifica que haya al menos un verbo después de la wake word
    return any(token in VERBOS for token in tokens[1:])