from PIL import Image
import qrcode

original_image = Image.open("merged_image.png")
original_image = original_image.convert("1")
original_image.save('merged_image.png')