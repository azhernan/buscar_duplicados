from .cli import app

def main():
    print('Proyecto ejecutado correctamente.')

#from buscar_duplicados import buscar_en_directorio

#if __name__ == "__main__":
#    buscar_en_directorio(".")

from .buscar_duplicados import buscar_duplicados, mostrar_duplicados_con_rich

if __name__ == "__main__":
    directorio = "data"  # o cualquier ruta que quieras probar
    duplicados = buscar_duplicados(directorio)
    mostrar_duplicados_con_rich(duplicados)
