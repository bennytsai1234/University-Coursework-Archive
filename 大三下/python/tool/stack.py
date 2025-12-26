from PIL import Image

# 要輸入的多張圖片的數量
num_images =322

# 創建一個空的圖片列表，用於存儲所有輸入圖片
input_images = []

# 開啟並添加所有輸入圖片到列表中
for i in range(1, num_images+1 ):
    image = Image.open(f'share_{i}.png')
    input_images.append(image)

# 確保所有輸入圖片的大小相同（使用第一張圖片的大小作為參考）
base_size = input_images[0].size

# 創建一張和輸入圖片大小相同的基底圖，初始設定為全白色
base_image = Image.new('1', base_size, color=255)

# 將所有輸入圖片疊加到基底圖上（使用位元運算）
for x in range(base_size[0]):
    for y in range(base_size[1]):
        result_pixel = 255  # 初始化為白色
        
        for image in input_images:
            pixel = image.getpixel((x, y))
            result_pixel &= pixel
        
        base_image.putpixel((x, y), result_pixel)

# 儲存生成的基底圖
base_image.save('merged_image.png')
