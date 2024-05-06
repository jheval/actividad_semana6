
def crear_archivo():
    try:
        nombre = input("Digite el nombre del archivo a crear: ")
        contenido = input("Digite el contenido que desea para el archivo: ")
        
        with open(nombre + ".txt", "wt") as archivo:
            archivo.write(contenido)
            
        print("¡Archivo creado exitosamente!")
    except Exception as e:
        print("Error al crear el archivo:", e)

# codigo



import os

def eliminar_archivo():
    archivo = input("Digite el nombre del archivo a eliminar (sin extensión): ")
    
    try:
        # Agregar la extensión .txt al nombre del archivo
        archivo = archivo + ".txt"
        
        # Verificar si el archivo existe antes de intentar borrarlo
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"El archivo {archivo} ha sido eliminado exitosamente.")
            return  # Salir de la función una vez que se elimina el archivo
        else:
            print(f"El archivo {archivo} no existe.")
    
    except OSError as e:
        print(f"Error al intentar eliminar el archivo {archivo}: {e}")

# codigo función eliminar_archivo() para ejecutarla




import os

def agregar_contenido():
    archivo_nombre = input("Digite el nombre del archivo que desea agregar contenido (sin extensión): ")
    
    try:
        # Agregar la extensión .txt al nombre del archivo
        archivo_nombre = archivo_nombre + ".txt"
        
        # Verificar si el archivo existe antes de intentar editarlo
        if os.path.exists(archivo_nombre):
            # Abrir el archivo en modo de escritura para añadir contenido
            with open(archivo_nombre, "a") as archivo:
                contenido = input("Digite el contenido a agregar: ")
                archivo.write("\n" +contenido)
            
            print(f"El archivo {archivo_nombre} ha sido editado exitosamente.")
        else:
            print(f"El archivo {archivo_nombre} no pudo ser editado porque no existe.")
            
    except OSError as e:
        print(f"Error al intentar editar el archivo {archivo_nombre}: {e}")

# codigo a la función agregar_contenido() para ejecutarla



import os

def mostrar_contenido():

    archivo_nombre = input("Digite el nombre del archivo que desea mostrar contenido (sin extensión): ")
    
    try:
        # Agregar la extensión .txt al nombre del archivo
        archivo_nombre = archivo_nombre + ".txt"
        
        # Verificar si el archivo existe antes de intentar mostrarlo
        if os.path.exists(archivo_nombre):
            # Abrir el archivo en modo de lectura de texto
            with open(archivo_nombre, "rt", encoding='utf8') as archivo:
                
                contenido = archivo.read()
                print(contenido)
            
        else:
            print(f"El archivo {archivo_nombre} no pudo ser mostrado porque no existe.")
            
    except OSError as e:
        print(f"Error al intentar mostrar el archivo {archivo_nombre}: {e}")

#  codigo a la función mostrar_contenido() para ejecutarla




if __name__ == "__main__":
    # Si el script se ejecuta directamente, esto se va a ejecutar
    pass




