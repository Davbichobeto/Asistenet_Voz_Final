"""
Módulo de Texto a Voz (TTS)
"""

import sys
import traceback

import pyttsx3

from asistente_voz.config import TTS_RATE, TTS_VOLUME, env_si


def hablar_sapi(texto: str) -> bool:
    try:
        import win32com.client
        sp = win32com.client.Dispatch("SAPI.SpVoice")
        sp.Volume = int(TTS_VOLUME * 100)
        sp.Rate = 0
        sp.Speak(texto)
        return True
    except:
        return False


class GeneradorVoz:
    def __init__(self) -> None:
        self._engine = None
        self._usar_sapi = sys.platform == "win32" and not env_si("ASISTENTE_TTS_PYTTSX3")

    def _inicializar_pyttsx3(self):
        if self._engine is not None:
            return
        try:
            self._engine = pyttsx3.init("sapi5" if sys.platform == "win32" else None)
            self._engine.setProperty("rate", TTS_RATE)
            self._engine.setProperty("volume", TTS_VOLUME)
        except Exception as e:
            print(f"⚠️ Error al inicializar TTS: {e}")
            self._engine = None

    def generar_voz(self, texto: str) -> None:
        if not texto or not texto.strip():
            return

        texto = texto.strip()
        print(f"🗣️ [TTS] {texto[:120]}...")

        if self._usar_sapi and hablar_sapi(texto):
            return

        self._inicializar_pyttsx3()
        if self._engine is None:
            return

        try:
            self._engine.say(texto)
            self._engine.runAndWait()
        except Exception as e:
            print(f"⚠️ Error en TTS: {e}")
            traceback.print_exc()