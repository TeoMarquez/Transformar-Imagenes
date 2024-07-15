from PIL import Image
import os

input_folder = "C:\\Users\\Mateo\\Desktop\\aa realizado"
output_folder = "C:\\Users\\Mateo\\Desktop\\aa realizado\\realizado"

# Asegúrate de que la carpeta de salida exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        img = Image.open(input_path)
        img = img.crop(img.getbbox())  # Elimina espacios en blanco
        img.save(output_path)
print("Proceso completo")
