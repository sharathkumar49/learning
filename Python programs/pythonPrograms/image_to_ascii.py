# Image to ASCII Art Converter
from PIL import Image

def image_to_ascii(path, width=100):
    chars = "@%#*+=-:. "
    img = Image.open(path).convert('L')
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, new_height))
    pixels = img.getdata()
    ascii_str = ""
    for i in range(len(pixels)):
        if i % width == 0:
            ascii_str += '\n'
        ascii_str += chars[pixels[i] * len(chars) // 256]
    return ascii_str

if __name__ == "__main__":
    path = input("Enter image path: ")
    print(image_to_ascii(path))
