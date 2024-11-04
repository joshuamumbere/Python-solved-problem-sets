from rembg import remove
from PIL import Image
input_path = '/home/masamba/Downloads/trial/p.webp'
output_path ='/home/masamba/Downloads/trial/p.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)