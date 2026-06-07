import os

_ENV_SI = frozenset({"1", "true", "yes", "si", "sí"})

def env_si(nombre: str) -> bool:
    return os.environ.get(nombre, "").strip().lower() in _ENV_SI

def _env_int(nombre: str, default: int) -> int:
    try:
        return int(os.environ.get(nombre, str(default)).strip())
    except ValueError:
        return default



LANGUAGE_STT: str = "es-MX"
TTS_RATE: int = 130
TTS_VOLUME: float = 1.0

LISTEN_TIMEOUT_S: int = 7
PHRASE_TIME_LIMIT_S: float = 10.0
AMBIENT_NOISE_DURATION_S: float = 1.0

MIC_DEVICE_INDEX: int | None = None

# WAKE WORDS MÁS FLEXIBLES
WAKE_WORDS: frozenset[str] = frozenset({
    "centauro", "centauros", "centauro"
})

VERBOS: frozenset[str] = frozenset({
    "reproduce", "reproducir", "busca", "buscar", "abre", "abrir", 
    "inicia", "lanza", "analiza"
})

POST_WELCOME_SILENCE_S: float = 0.4