import qrcode

data = "時間就是金錢"

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, 
    border=0,    
)

# 將數據添加到QR碼
qr.add_data(data)
qr.make(fit=True)

# 創建QR碼圖片
img = qr.make_image(fill_color="black", back_color="white")

# 儲存QR碼圖片
img.save("qrcode.png")

