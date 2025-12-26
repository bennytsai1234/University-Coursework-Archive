from PIL import Image


# 打开原始图像
img = Image.open("ncnu1.png")

# 获取原始图像的大小
orig_width, orig_height = img.size

# 设置新的尺寸
new_width, new_height = 66, 66

# 放大图像尺寸,不使用任何滤波器
new_img = img.resize((new_width, new_height), resample=Image.NEAREST)
new_img.convert("1")
# 保存新图像
new_img.save("ncnu1.png")
