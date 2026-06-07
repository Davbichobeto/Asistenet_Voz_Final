"""
Módulo de Acciones - Centauro
"""

import subprocess
import threading
import webbrowser
from urllib.parse import quote_plus

import pywhatkit

from asistente_voz.voz_tts import GeneradorVoz


def hablar(voz: GeneradorVoz, mensaje: str):
    print(f"🗣️ {mensaje}")
    voz.generar_voz(mensaje)


OFFICE_APPS = {
    "word": "WINWORD.EXE", "documento": "WINWORD.EXE",
    "excel": "EXCEL.EXE", "hoja": "EXCEL.EXE",
    "powerpoint": "POWERPNT.EXE", "presentación": "POWERPNT.EXE", "ppt": "POWERPNT.EXE",
    "outlook": "OUTLOOK.EXE", "correo": "OUTLOOK.EXE",
    "access": "MSACCESS.EXE", "onenote": "ONENOTE.EXE",
    "clima": "https://www.meteored.mx/clima_Ciudad+General+Escobedo-America+Norte-Mexico-Nuevo+Leon--1-71315.html:",
    "mapas": "https://www.google.com/maps",
}


def procesar_accion(verbo: str, cola: list[str], voz: GeneradorVoz):
    texto = " ".join(cola).strip()

    if verbo in ("abre", "abrir", "inicia", "lanza"):
        # 1. Compara lo que escuchó con tu diccionario OFFICE_APPS
        app_encontrada = next((OFFICE_APPS[k] for k in OFFICE_APPS if k in texto.lower()), None)
        
        if app_encontrada:
            hablar(voz, "Abriendo aplicación...")
            try:
                # 2. Ahora sí ejecuta el archivo .EXE correcto (ej. start WINWORD.EXE)
                subprocess.Popen(f"start {app_encontrada}", shell=True)
            except:
                hablar(voz, "No pude abrir esa aplicación.")
        else:
            hablar(voz, f"No tengo el programa registrado para: {texto}")

    elif verbo in ("busca", "buscar"):
        hablar(voz, f"Buscando {texto}.")
        webbrowser.open(f"https://www.google.com/search?q={quote_plus(texto)}")

    elif verbo in ("reproduce", "reproducir"):
        hablar(voz, f"Reproduciendo {texto} en YouTube.")
        def _play_on_yt(query: str):
            try:
                # Intentar usar playonyt si está disponible
                play = getattr(pywhatkit, "playonyt", None)
                if callable(play):
                    play(query)
                else:
                    # Fallback: abrir búsqueda de YouTube en el navegador
                    webbrowser.open(f"https://www.youtube.com/results?search_query={quote_plus(query)}")
            except Exception:
                webbrowser.open(f"https://www.youtube.com/results?search_query={quote_plus(query)}")

        threading.Thread(target=lambda: _play_on_yt(texto), daemon=True).start()

    elif verbo == "analiza":
        hablar(voz, "Iniciando sistema experto.")
        subprocess.Popen(["python", "Base_Hechos.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

    else:
        hablar(voz, "Comando recibido.")