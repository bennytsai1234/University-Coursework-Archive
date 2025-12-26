import cv2
from pyzbar.pyzbar import decode

def decode_qrcode_opencv(image_path):
    # 讀取圖片
    image = cv2.imread(image_path)

    # 將圖片轉換為灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用 pyzbar 解碼
    barcodes = decode(gray)

    # 顯示解碼結果
    if barcodes:
        for barcode in barcodes:
            print('Data:', barcode.data.decode('utf-8'))
            print('Type:', barcode.type)
    else:
        print("false")

decode_qrcode_opencv('merged_image.png')
