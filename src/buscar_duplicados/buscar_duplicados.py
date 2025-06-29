import os
import hashlib
from collections import defaultdict
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from rich.console import Console
from rich.table import Table

def calcular_hash(archivo, bloque=65536):
    """Calcula el hash MD5 de un archivo."""
    hash_md5 = hashlib.md5()
    try:
        with open(archivo, "rb") as f:
            for bloque_bytes in iter(lambda: f.read(bloque), b""):
                hash_md5.update(bloque_bytes)
    except (PermissionError, FileNotFoundError):
        return None, archivo
    return hash_md5.hexdigest(), archivo

def buscar_duplicados(directorio_base):
    """Busca archivos duplicados por hash con concurrencia."""
    archivos = []
    for ruta, _, nombres in os.walk(directorio_base):
        for nombre in nombres:
            archivos.append(os.path.join(ruta, nombre))

    hash_dict = defaultdict(list)
    with ThreadPoolExecutor() as executor:
        tareas = {executor.submit(calcular_hash, archivo): archivo for archivo in archivos}
        for tarea in tqdm(as_completed(tareas), total=len(tareas), desc="Procesando archivos"):
            hash_resultado, archivo = tarea.result()
            if hash_resultado:
                hash_dict[hash_resultado].append(archivo)

    # Filtrar duplicados
    return {h: r for h, r in hash_dict.items() if len(r) > 1}

def mostrar_duplicados(duplicados):
    """Imprime los archivos duplicados encontrados."""
    if not duplicados:
        print("No se encontraron archivos duplicados.")
        return

    print("Archivos duplicados encontrados:\n")
    for hash_, paths in duplicados.items():
        print(f"Hash {hash_[:8]}...")
        for p in paths:
            print(f"   - {p}")
        print()

def buscar_en_directorio(directorio):
    """Función principal para ejecutar desde main."""
    print(f"🔍 Buscando archivos duplicados en: {directorio}")
    duplicados = buscar_duplicados(directorio)
    mostrar_duplicados(duplicados)


def mostrar_duplicados_con_rich(duplicados):
    console = Console()

    if not duplicados:
        console.print("[bold green] No se encontraron archivos duplicados.[/bold green]")
        return

    table = Table(title="Archivos duplicados", show_lines=True)
    table.add_column("Hash", style="cyan", no_wrap=True)
    table.add_column("Archivos", style="magenta")

    for hash_, archivos in duplicados.items():
        paths_formateados = "\n".join(archivos)
        table.add_row(hash_[:8] + "...", paths_formateados)

    console.print(table)


