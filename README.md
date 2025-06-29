# 🔍 Buscar Duplicados

Una herramienta en Python para buscar y eliminar archivos duplicados en un directorio, con salida elegante y CLI robusta.

## 🚀 Características

- Detección de archivos duplicados por hash (MD5)
- Interfaz de línea de comandos (CLI) con `typer`
- Barra de progreso con `tqdm`
- Visualización de resultados con `rich`
- Eliminación opcional de duplicados (`--delete`)
- Estructura profesional con `poetry`
- Entrada principal: `buscar-duplicados`

## 🧰 Requisitos

- Python >= 3.12
- [Poetry](https://python-poetry.org/) instalado

## ⚙️ Instalación

```bash
git clone https://github.com/azhernan/buscar_duplicados.git
cd buscar_duplicados
poetry install
```

> Si ocurre un error por codificación, asegurate de que todos los archivos estén guardados en UTF-8 sin BOM.

## 🧪 Uso

Escanear una carpeta:

```bash
poetry run buscar-duplicados "C:/Ruta/Al/Directorio"
```

Escanear y eliminar duplicados automáticamente:

```bash
poetry run buscar-duplicados "C:/Ruta/Al/Directorio" --delete
```

Ver ayuda:

```bash
poetry run buscar-duplicados --help
```

## 📁 Estructura del Proyecto

```
buscar_duplicados/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   └── buscar_duplicados.py
│
├── .vscode/              # Configuración de entorno en VSCode
├── data/                 # Carpeta para datos
├── notebooks/            # Jupyter Notebooks (si aplica)
├── README.md
├── requirements.txt
├── pyproject.toml        # Configuración de Poetry
└── poetry.lock
```

## 🧠 Autor

**Hernán Velázquez**  
📧 [azhernan@hotmail.com](mailto:azhernan@hotmail.com)  
🔗 [GitHub](https://github.com/azhernan)

---

¡Contribuciones, sugerencias y estrellas son bienvenidas! ⭐
