from zxing import BarCodeReader

def decode_qrcode_zxing(image_path):
    # 初始化BarCodeReader
    reader = BarCodeReader()

    # 讀取圖片
    barcode = reader.decode(image_path)

    # 顯示解碼結果
    if barcode:
        print('Data:', barcode.raw)
        print('Type:', barcode.format)
    else:
        print("false")


decode_qrcode_zxing('merged_image.png')
