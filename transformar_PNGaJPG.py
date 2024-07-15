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

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        img = Image.open(input_path)
        img = img.convert("RGB")  # Convertir a modo RGB antes de guardar como JPG
        img.save(output_path, "JPEG")

print("Conversión completa.")
