import sys
from pathlib import Path


ruta_raiz = Path(__file__).resolve().parent

if str(ruta_raiz) not in sys.path:
    sys.path.insert(0, str(ruta_raiz))

# Delegamos el control al agente de voz
try:
    from agente import main as agente_main
except ImportError as e:
    print(f"Error: No se pudo encontrar el módulo. {e}")
    sys.exit(1)

if __name__ == "__main__":
    agente_main()