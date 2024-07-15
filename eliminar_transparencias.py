from PIL import Image
import os
from tkinter import Tk, filedialog

def select_folder(prompt):
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title=prompt)
    root.destroy()
    return folder_selected

input_folder = select_folder("Selecciona la carpeta de entrada")
output_folder = select_folder("Selecciona la carpeta de salida")

# Lista las imágenes PNG en la carpeta de entrada
image_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".png")]


for filename in image_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)
    
    img = Image.open(input_path)
    bbox = img.getbbox()  # Obtén la caja delimitadora que encierra el contenido de la imagen
    
    # Verifica si la caja delimitadora es válida
    if bbox:
        print(f"Procesando: {filename}")
        img = img.crop(bbox)  # Recorta la imagen al contenido
        img.save(output_path)
    else:
        print(f"Saltando: {filename} (sin contenido visible)")

print("Proceso completo")
