"""
Sistema Experto: Identificación de Animales
Parte del Asistente centauro
"""

from __future__ import annotations


BASE_DE_CONOCIMIENTOS = {
    "Perro": ["ladra", "juega", "pelaje", "domesticado", "obedece"],
    "Gato": ["rasca", "juega", "maulla", "independiente", "pelaje"],
    "Pájaro": ["plumas", "pico", "vuela", "canta", "domesticado"],
    "Pez": ["branquias", "escamas", "nada", "aletas"],
    "Serpiente": ["reptil", "escamas", "se arrastra", "no tiene patas"],
    "Tigre": ["garras", "pelaje", "caza", "salvaje"],
    "León": ["melena", "rugido", "salvaje", "carnívoro", "felino"],
    "Elefante": ["trompa", "colmillos", "orejas grandes", "gris", "mamífero"],
    "Jirafa": ["cuello largo", "manchas", "alta", "herbívoro", "sabana"],
    "Mono": ["trepa", "inteligente", "cola", "selva", "plátanos"],
    "Oso": ["hiberna", "pelaje", "garras", "omnívoro", "grande"],
    "Lobo": ["aúlla", "manada", "salvaje", "carnívoro", "bosque"],
    "Zorro": ["astuto", "pelaje rojizo", "cola esponjosa", "salvaje", "omnívoro"],
    "Caballo": ["galopa", "crin", "montura", "relincha", "herbívoro"],
    "Vaca": ["leche", "muge", "cuernos", "granja", "herbívoro"],
    "Cerdo": ["gruñe", "rosado", "granja", "lodo", "omnívoro"],
    "Oveja": ["lana", "bala", "rebaño", "granja", "herbívoro"],
    "Cabra": ["cuernos", "barba", "escala", "granja", "bala"],
    "Conejo": ["orejas largas", "salta", "zanahorias", "madriguera", "rápido"],
    "Ratón": ["pequeño", "queso", "roedor", "cola larga", "ruiditos"],
    "Murciélago": ["vuela", "nocturno", "ecolocalización", "cuevas", "colgado"],
    "Águila": ["visión aguda", "vuela alto", "garras", "pico curvo", "cazadora"],
    "Búho": ["nocturno", "gira la cabeza", "ojos grandes", "ulula", "cazador"],
    "Pingüino": ["no vuela", "nada", "blanco y negro", "hielo", "pescado"],
    "Avestruz": ["corre rápido", "no vuela", "cuello largo", "huevos grandes", "alta"],
    "Loro": ["habla", "colores", "pico curvo", "plumas", "selva"],
    "Pato": ["grazna", "nada", "plumas", "estanque", "pico plano"],
    "Gallina": ["cacarea", "huevos", "granja", "plumas", "pico"],
    "Rana": ["croa", "salta", "anfibio", "verde", "insectos"],
    "Sapo": ["verrugas", "croa", "terrestre", "anfibio", "lento"],
    "Cocodrilo": ["mandíbulas", "escamas", "reptil", "agua", "peligroso"],
    "Tortuga": ["caparazón", "lenta", "reptil", "longeva", "terrestre o marina"],
    "Iguana": ["escamas", "verde", "cresta", "reptil", "sol"],
    "Camaleón": ["cambia de color", "ojos independientes", "lengua larga", "reptil", "lento"],
    "Araña": ["ocho patas", "telaraña", "insectos", "venenosa", "arácnido"],
    "Escorpión": ["aguijón", "veneno", "pinzas", "desierto", "arácnido"],
    "Abeja": ["miel", "zumba", "poliniza", "amarilla y negra", "aguijón"],
    "Mariposa": ["alas coloridas", "metamorfosis", "vuela", "néctar", "insecto"],
    "Hormiga": ["trabajadora", "colonia", "pequeña", "fuerte", "insecto"],
    "Tiburón": ["aletas", "dientes", "océano", "depredador", "branquias"],
    "Delfín": ["inteligente", "salta", "océano", "ecolocalización", "mamífero"],
    "Ballena": ["gigante", "océano", "espiráculo", "canta", "mamífero"],
    "Pulpo": ["ocho tentáculos", "tinta", "océano", "inteligente", "camuflaje"],
    "Cangrejo": ["pinzas", "camina de lado", "caparazón", "playa", "marino"],
    "Medusa": ["transparente", "tentáculos", "pica", "océano", "gelatinosa"],
    "Estrella de mar": ["cinco brazos", "fondo marino", "regenera", "lenta", "marina"],
    "Hipopótamo": ["pesado", "boca grande", "río", "África", "mamífero"],
    "Rinoceronte": ["cuerno", "piel gruesa", "pesado", "herbívoro", "África"],
    "Cebra": ["rayas", "blanco y negro", "África", "manada", "herbívoro"],
    "Canguro": ["salta", "bolsa", "Australia", "cola fuerte", "herbívoro"],
    "Koala": ["eucalipto", "trepa", "Australia", "lento", "marsupial"],
    "Oso Panda": ["blanco y negro", "bambú", "Asia", "pelaje", "lento"],
    "Camello": ["jorobas", "desierto", "resistente", "arena", "herbívoro"],
    "Ardilla": ["nueces", "trepa", "cola esponjosa", "roedor", "rápida"],
    "Castor": ["presa", "madera", "dientes fuertes", "cola plana", "roedor"],
    "Mapache": ["antifaz", "cola anillada", "nocturno", "basura", "omnívoro"],

}


def _normalizar(texto: str) -> str:
    """Normaliza texto: minúsculas y sin acentos."""
    s = texto.strip().lower()
    reemplazos = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ü", "u"), ("ñ", "n")]
    for a, b in reemplazos:
        s = s.replace(a, b)
    return s


def obtener_caracteristicas() -> list[str]:
    """Pide características al usuario."""
    print("\n🎯 Sistema Experto - Identificación de Animales")
    print("Ingresa entre 1 y 4 características (escribe 'fin' para terminar):")

    caracteristicas: list[str] = []
    while len(caracteristicas) < 4:
        entrada = input(f"Característica #{len(caracteristicas) + 1}: ").strip()
        if _normalizar(entrada) == "fin":
            break
        norm = _normalizar(entrada)
        if norm and norm not in caracteristicas:
            caracteristicas.append(norm)
        else:
            print("❌ Ingresa una característica válida y única.")

    if not caracteristicas:
        print("Debes ingresar al menos una característica.")
        return obtener_caracteristicas()

    return caracteristicas


def _f1_coincidencia(usuario: set[str], animal: set[str]) -> tuple[float, int]:
    """Calcula similitud usando métrica F1."""
    if not usuario or not animal:
        return 0.0, 0
    inter = usuario & animal
    coincidencias = len(inter)
    if coincidencias == 0:
        return 0.0, 0

    precision = coincidencias / len(usuario)
    recall = coincidencias / len(animal)
    f1 = 2 * precision * recall / (precision + recall)
    return f1 * 100.0, coincidencias


def inferir_animal(caracteristicas: list[str]) -> list[tuple[str, float, int]]:
    """Devuelve animales ordenados por coincidencia."""
    usuario = {_normalizar(c) for c in caracteristicas}
    resultados = []

    for nombre, rasgos in BASE_DE_CONOCIMIENTOS.items():
        conjunto_animal = {_normalizar(r) for r in rasgos}
        score, matches = _f1_coincidencia(usuario, conjunto_animal)
        resultados.append((nombre, score, matches))

    resultados.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return resultados


def main() -> None:
    print("=" * 60)
    print("🐾 SISTEMA EXPERTO DE IDENTIFICACIÓN DE ANIMALES")
    print("=" * 60)

    caracteristicas = obtener_caracteristicas()
    print(f"\nCaracterísticas ingresadas: {', '.join(caracteristicas)}")

    resultados = inferir_animal(caracteristicas)

    print("\n🔍 Resultados (ordenados por coincidencia):")
    hay_coincidencia = False
    for animal, puntaje, coinc in resultados:
        if puntaje > 0:
            hay_coincidencia = True
            print(f"• {animal}: {puntaje:.1f}% ({coinc} rasgo(s) coincidente(s))")

    if not hay_coincidencia:
        print("❌ No hubo coincidencias claras. Intenta con otros rasgos.")


if __name__ == "__main__":
    main()