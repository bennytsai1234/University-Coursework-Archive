from PIL import Image

# 打开原始图像
img = Image.open("ncnu.png")

# 获取原始图像的大小
orig_width, orig_height = img.size

# 计算新尺寸的比例
new_width, new_height = 33, 33
ratio = min(new_width/orig_width, new_height/orig_height)

# 计算新尺寸
new_size = (int(orig_width*ratio), int(orig_height*ratio))

# 调整图像尺寸,使用LANCZOS重采样滤波器
img = img.resize(new_size, resample=Image.Resampling.LANCZOS)

# 创建一个新的空白图像
new_img = Image.new("RGB", (new_width, new_height))

# 将调整后的图像粘贴到新图像上
x = (new_width - new_size[0]) // 2
y = (new_height - new_size[1]) // 2
new_img.paste(img, (x, y))

# 保存新图像
new_img.save("ncnu2.png")