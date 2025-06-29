from PIL import Image
import os

def reducir_imagen(ruta_entrada, ruta_salida, ancho_nuevo=None, alto_nuevo=None, porcentaje=None):
    """
    Reduce el tamaño de una imagen manteniendo la relación de aspecto.
    
    Args:
        ruta_entrada (str): Ruta de la imagen original
        ruta_salida (str): Ruta donde guardar la imagen reducida
        ancho_nuevo (int, optional): Ancho deseado en píxeles
        alto_nuevo (int, optional): Alto deseado en píxeles
        porcentaje (float, optional): Porcentaje de reducción (0-100)
        
    Nota:
        Solo debe especificarse ancho_nuevo, alto_nuevo O porcentaje, no varios.
        Si no se especifica ninguno, se pedirá por consola.
    """
    try:
        # Abrir la imagen original
        with Image.open(ruta_entrada) as img:
            ancho_original, alto_original = img.size
            
            # Determinar las nuevas dimensiones
            if porcentaje is not None:
                factor = porcentaje / 100.0
                ancho_nuevo = int(ancho_original * factor)
                alto_nuevo = int(alto_original * factor)
            elif ancho_nuevo is not None and alto_nuevo is not None:
                pass  # Usar los valores proporcionados
            elif ancho_nuevo is not None:
                # Calcular alto manteniendo relación de aspecto
                relacion = alto_original / ancho_original
                alto_nuevo = int(ancho_nuevo * relacion)
            elif alto_nuevo is not None:
                # Calcular ancho manteniendo relación de aspecto
                relacion = ancho_original / alto_original
                ancho_nuevo = int(alto_nuevo * relacion)
            else:
                # Pedir parámetros por consola
                print(f"Tamaño actual: {ancho_original}x{alto_original} px")
                opcion = input("Reducir por [1]porcentaje, [2]ancho, [3]alto, [4]ambos: ")
                
                if opcion == "1":
                    porcentaje = float(input("Porcentaje de reducción (ej. 50 para 50%): "))
                    factor = porcentaje / 100.0
                    ancho_nuevo = int(ancho_original * factor)
                    alto_nuevo = int(alto_original * factor)
                elif opcion == "2":
                    ancho_nuevo = int(input("Nuevo ancho en px: "))
                    relacion = alto_original / ancho_original
                    alto_nuevo = int(ancho_nuevo * relacion)
                elif opcion == "3":
                    alto_nuevo = int(input("Nuevo alto en px: "))
                    relacion = ancho_original / alto_original
                    ancho_nuevo = int(alto_nuevo * relacion)
                elif opcion == "4":
                    ancho_nuevo = int(input("Nuevo ancho en px: "))
                    alto_nuevo = int(input("Nuevo alto en px: "))
                else:
                    print("Opción no válida")
                    return
            
            # Redimensionar la imagen
            img_redimensionada = img.resize((ancho_nuevo, alto_nuevo), Image.LANCZOS)
            
            # Guardar la imagen
            img_redimensionada.save(ruta_salida)
            print(f"Imagen reducida guardada en: {ruta_salida}")
            print(f"Tamaño original: {ancho_original}x{alto_original} px")
            print(f"Tamaño nuevo: {ancho_nuevo}x{alto_nuevo} px")
            
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    # Ejemplo de uso
    ruta_entrada = input("Ruta de la imagen original: ").strip('"')
    ruta_salida = input("Ruta para guardar la imagen reducida: ").strip('"')
    
    # Verificar si la ruta de entrada existe
    if not os.path.exists(ruta_entrada):
        print("Error: El archivo de entrada no existe.")
    else:
        # Llamar a la función sin parámetros de tamaño para que pregunte por consola
        reducir_imagen(ruta_entrada, ruta_salida)