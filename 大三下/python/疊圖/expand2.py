from PIL import Image
import random
qr_code_image = Image.open("qrcode.png")
original_image = Image.open("ncnu1.png")

qr_code_bw = qr_code_image.convert("1")
original_image_bw = original_image.convert("1")
width, height = qr_code_bw.size
width2, height2 = original_image_bw.size

H = [["□" for _ in range(width2)] for _ in range(height2)]
for x in range(0, width2):
    for y in range(0, height2):
        if x < width and y < height:
            if qr_code_bw.getpixel((x, y)) == 0:
                H[x][y] = "∎"



def adjust_color(image):
    adjusted_image = image.copy()
    pixels = adjusted_image.load()
    adjusted_image2 = image.copy()
    pixels2 = adjusted_image2.load()
    count = 0
    for x in range(0, width - 1, 2):
        for y in range(0, height - 1, 2):
            if (
                H[x][y] == "∎"
                and H[x + 1][y] == "∎"
                and H[x][y + 1] == "∎"
                and H[x + 1][y + 1] == "∎"
            ):
                if (
                    original_image_bw.getpixel((x, y)) == 0
                    and original_image_bw.getpixel((x + 1, y)) == 0
                    and original_image_bw.getpixel((x, y + 1)) == 0
                    and original_image_bw.getpixel((x + 1, y + 1)) == 0
                ):

                    pixels2[x, y] = 0
                    pixels2[x + 1, y] = 0
                    pixels2[x, y + 1] = 0
                    pixels2[x + 1, y + 1] = 0
                    pixels[x, y] = 255
                    pixels[x + 1, y] = 255
                    pixels[x, y + 1] = 255
                    pixels[x + 1, y + 1] = 255
                    count = count + 1
            if (
                H[x][y] == "∎"
                and H[x + 1][y] == "∎"
                and H[x][y + 1] == "∎"
                and H[x + 1][y + 1] == "∎"
            ):
                if (
                    original_image_bw.getpixel((x, y)) == 255
                    and original_image_bw.getpixel((x + 1, y)) == 255
                    and original_image_bw.getpixel((x, y + 1)) == 255
                    and original_image_bw.getpixel((x + 1, y + 1)) == 255
                ):

                    pixels2[x, y] = 255
                    pixels2[x + 1, y] = 255
                    pixels2[x, y + 1] = 255
                    pixels2[x + 1, y + 1] = 255
                    pixels[x, y] = 0
                    pixels[x + 1, y] = 0
                    pixels[x, y + 1] = 0
                    pixels[x + 1, y + 1] = 0
                    count = count + 1

            if (
                H[x][y] == "□"
                and H[x + 1][y] == "□"
                and H[x][y + 1] == "□"
                and H[x + 1][y + 1] == "□"
            ):
                if (
                    original_image_bw.getpixel((x, y)) == 0
                    and original_image_bw.getpixel((x + 1, y)) == 0
                    and original_image_bw.getpixel((x, y + 1)) == 0
                    and original_image_bw.getpixel((x + 1, y + 1)) == 0
                ):
                    zero_indices = random.sample(range(4), 1)  # 選擇兩個索引位置
                    for i in range(4):
                        if i in zero_indices:
                            if i == 0:
                                a = 0
                            elif i == 1:
                                b = 0
                            elif i == 2:
                                c = 0
                            else:
                                d = 0
                        else:
                            if i == 0:
                                a = 255
                            elif i == 1:
                                b = 255
                            elif i == 2:
                                c = 255
                            else:
                                d = 255
                    pixels2[x, y] = a
                    pixels2[x + 1, y] = b
                    pixels2[x, y + 1] = c
                    pixels2[x + 1, y + 1] = d
                    pixels[x, y] = 255
                    pixels[x + 1, y] = 255
                    pixels[x, y + 1] = 255
                    pixels[x + 1, y + 1] = 255
                    count = count + 1
            if (
                H[x][y] == "□"
                and H[x + 1][y] == "□"
                and H[x][y + 1] == "□"
                and H[x + 1][y + 1] == "□"
            ):
                if (
                    original_image_bw.getpixel((x, y)) == 255
                    and original_image_bw.getpixel((x + 1, y)) == 255
                    and original_image_bw.getpixel((x, y + 1)) == 255
                    and original_image_bw.getpixel((x + 1, y + 1)) == 255
                ):
                    zero_indices = random.sample(range(4), 1)  # 選擇兩個索引位置
                    for i in range(4):
                        if i in zero_indices:
                            if i == 0:
                                a = 0
                            elif i == 1:
                                b = 0
                            elif i == 2:
                                c = 0
                            elif i == 3:
                                d = 0
                        else:
                            if i == 0:
                                a = 255
                            elif i == 1:
                                b = 255
                            elif i == 2:
                                c = 255
                            elif i == 3:
                                d = 255
                    pixels2[x, y] = 255
                    pixels2[x + 1, y] = 255
                    pixels2[x, y + 1] = 255
                    pixels2[x + 1, y + 1] = 255
                    pixels[x, y] = a
                    pixels[x + 1, y] = b
                    pixels[x, y + 1] = c
                    pixels[x + 1, y + 1] = d
                    count = count + 1
    return adjusted_image, adjusted_image2


adjusted_image1, adjusted_image2 = adjust_color(original_image)
adjusted_image1.save("share_1.png")
adjusted_image2.save("share_2.png")
