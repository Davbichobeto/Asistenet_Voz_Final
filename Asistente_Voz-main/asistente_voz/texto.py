import string

def normalize(texto: str) -> str:
    if not texto:
        return ""
    s = texto.strip().lower()
    # Normalización 
    reemplazos = [
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("ü", "u"), ("ñ", "n"), ("¡", ""), ("!", ""), ("¿", ""), ("?", "")
    ]
    for a, b in reemplazos:
        s = s.replace(a, b)
    return s

def tokenizar(comando_normalizado: str) -> list[str]:
    borde = string.punctuation + "¿¡«»"
    tokens = [t for t in (w.strip(borde) for w in comando_normalizado.split()) if t]
    return tokens

def poner_wake_word_primera(tokens: list[str], wake_words: frozenset[str], verbos: frozenset[str]) -> list[str]:
    """Versión mucho más tolerante para detectar centauro"""
    if not tokens:
        return tokens

    # Buscar cualquier variación de Centauro en toda la frase
    for i, token in enumerate(tokens):
        token_norm = token.lower()
        if any(w in token_norm for w in ["centauro", "centauros"]):
            # Reordenar poniendo la wake word primero
            return [token] + tokens[:i] + tokens[i+1:]
    
    # Si no encuentra Centauro, devolver tal cual (para depuración)
    return tokens