"""
Agente Principal del Asistente de Voz centauro
Versión con detección de Wake Word más tolerante
"""

import time

from asistente_voz.acciones import procesar_accion
from asistente_voz.config import (
    POST_WELCOME_SILENCE_S,
    VERBOS,
    WAKE_WORDS,
)
from asistente_voz.gramatica import comando_valido_según_gramatica
from asistente_voz.texto import normalize, tokenizar
from asistente_voz.voz_stt import ReconocimientoVoz
from asistente_voz.voz_tts import GeneradorVoz


def contiene_wake_word(tokens: list[str]) -> bool:
    """Busca si existe alguna variación de centauro en los tokens."""
    for token in tokens:
        t = token.lower()
        if any(w in t for w in ["centauro", "centauros", "centauro"]):
            return True
    return False


def extraer_comando(tokens: list[str]) -> tuple[str | None, list[str]]:
    """Extrae verbo y resto del comando."""
    for i, tok in enumerate(tokens):
        if tok in VERBOS:
            return tok, tokens[i+1:]
    return None, []


def procesar_comando(comando_normalizado: str, voz: GeneradorVoz) -> None:
    tokens = tokenizar(comando_normalizado)
    print(f"→ Tokens detectados: {tokens}")   

    if not tokens:
        return


    if not contiene_wake_word(tokens):
        voz.generar_voz("Por favor inicia el comando con Centauro.")
        return

    # Verificar que haya un verbo
    verbo, cola = extraer_comando(tokens)
    
    if verbo is None:
        voz.generar_voz("No entendí qué acción quieres realizar.")
        return

    # Ejecutar la acción
    procesar_accion(verbo, cola, voz)


def main() -> None:
    print("🚀 Iniciando Asistente de Voz Centauro")
    
    voz = GeneradorVoz()
    escucha = ReconocimientoVoz()

    voz.generar_voz("Hola, soy Centauro.")
    voz.generar_voz("Estoy lista.")
    
    if POST_WELCOME_SILENCE_S > 0:
        time.sleep(POST_WELCOME_SILENCE_S)

    print("\n🎤 Di 'Centauro' seguido de tu comando.\n")

    try:
        while True:
            texto_crudo = escucha.escuchar_audio()
            if not texto_crudo:
                continue

            comando = normalize(texto_crudo)
            print(f"\n📝 Texto reconocido: {comando}")
            
            procesar_comando(comando, voz)

    except KeyboardInterrupt:
        print("\n\n👋 Saliendo...")
        voz.generar_voz("Hasta luego.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
    