from PIL import Image
import os

input_folder = r"C:\Users\Mateo\Desktop\aa realizado"
output_folder = r"C:\Users\Mateo\Desktop\aa realizado\realizado"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")

        img = Image.open(input_path)
        img.save(output_path, "PNG")

print("Conversión completa.")
