import typer
from .buscar_duplicados import buscar_duplicados, mostrar_duplicados_con_rich
from pathlib import Path
import os

app = typer.Typer(help="Herramienta para detectar archivos duplicados")

@app.command()
def scan(
    path: Path = typer.Argument(
        default=Path("."),
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Ruta del directorio a escanear"
    ),
    delete: bool = typer.Option(
        False,
        "--delete",
        help="Eliminar duplicados (mantiene solo uno)"
    )
):
    """
    Busca archivos duplicados en un directorio.
    """
    if not path.exists() or not path.is_dir():
        typer.secho("❌ Ruta inválida.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    duplicados = buscar_duplicados(str(path))

    if not duplicados:
        typer.secho("✔ No se encontraron archivos duplicados.", fg=typer.colors.GREEN)
        raise typer.Exit()

    mostrar_duplicados_con_rich(duplicados)

    if delete:
        for archivos in duplicados.values():
            for archivo in archivos[1:]:
                try:
                    os.remove(archivo)
                    typer.echo(f"🗑️ Eliminado: {archivo}")
                except Exception as e:
                    typer.secho(f"⚠️ Error al eliminar {archivo}: {e}", fg=typer.colors.YELLOW)
        typer.secho("✅ Duplicados eliminados.", fg=typer.colors.GREEN)

if __name__ == "__main__":
    app()
