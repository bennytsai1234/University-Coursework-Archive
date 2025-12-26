from PIL import Image
import random

# 開啟QR碼圖像
qr_code = Image.open('qrcode.png')

# 確定要創建的圖片數量
num_images = 4

# 確定要創建的四張圖片的大小，與QR碼圖像相同
width, height = qr_code.size

# define box_size
box_size = 10

# 創建指定數量的空白圖片
output_images = [Image.new('1', (width, height), color=255) for _ in range(num_images)]


# 將QR碼中的黑色方塊隨機分配到指定數量的圖片中，保持方塊大小
for x in range(0, width, box_size):
    for y in range(0, height, box_size):
        pixel_value = qr_code.getpixel((x, y))
        if pixel_value == 0:  # 如果是黑色方塊
            random_index = random.randint(0, num_images - 1)  # 隨機選擇一張圖片
            # 將整個方塊設置為黑色
            for i in range(box_size):
                for j in range(box_size):
                    output_images[random_index].putpixel((x + i, y + j), 0)

# 儲存指定數量的圖片
for i, output_image in enumerate(output_images):
    output_image.save(f'output_{i + 1}.png')



