from PIL import Image

original_image = Image.open("ncnu2.png")

original_image_bw = original_image.convert("1")
width, height = original_image_bw.size


def adjust_color(image):
    adjusted_image = image.copy()
    pixels = adjusted_image.load()
    for x in range(0, width-1, 2):
        for y in range(0, height-1, 2):
            if original_image_bw.getpixel((x, y)) == 0 | original_image_bw.getpixel((x, y)) == 0| original_image_bw.getpixel((x, y)) == 0| original_image_bw.getpixel((x, y)) == 0:
                pixels[x, y] = 255
                pixels[x+1, y] = 255
                pixels[x, y+1] = 255
                pixels[x+1, y+1] = 255
            else:    
                pixels[x, y] = 0
                pixels[x+1, y] = 0
                pixels[x, y+1] = 0
                pixels[x+1, y+1] = 0

    return adjusted_image
adjusted_image = adjust_color(original_image)
adjusted_image.save('ncnu1.png')
