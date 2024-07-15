from PIL import Image
import os

input_folder = "ruta/a/tu/carpeta/de/imagenes"
output_folder = "ruta/a/tu/carpeta/de/salida"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        img = Image.open(input_path)
        img = img.convert("RGB")  # Convertir a modo RGB antes de guardar como JPG
        img.save(output_path, "JPEG")

print("Conversión completa.")