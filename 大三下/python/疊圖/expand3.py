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






H = [["□" for _ in range(width)] for _ in range(height  )]
for x in range(0, width ):
    for y in range(0, height):
        black_pixel_found = any(
            qr_code_bw.getpixel((x + i, y + j)) == 0
            for i in range()
            for j in range()
        )
        if black_pixel_found:
            H[x ][y] = "∎"


# 定義 block
block1 = [
    ["□" for _ in range(width)] for _ in range(height )
]
block2 = [
    ["□" for _ in range(width)] for _ in range(height )
]
block3 = [
    ["□" for _ in range(width)] for _ in range(height )
]
block4 = [
    ["□" for _ in range(width)] for _ in range(height )
]
remainingblackmodule = [
    ["□" for _ in range(width)] for _ in range(height )
]

# 定義 block data
data_words = []
ecc_words = []
for _ in range(36):
    data_word = [["□" for _ in range(width)]
                 for _ in range(height )]
    data_words.append(data_word)

for _ in range(64):
    ecc_word = [["□" for _ in range(width)]
                for _ in range(height )]
    ecc_words.append(ecc_word)
# 1
# 1
for x in range(31, 33):
    for y in range(29, 33):
        data_words[0][x][y] = H[x][y]

for x in range(31, 33):
    for y in range(25, 29):
        data_words[9][x][y] = H[x][y]

for x in range(31, 33):
    for y in range(21, 25):
        data_words[18][x][y] = H[x][y]

for x in range(31, 33):
    for y in range(17, 21):
        data_words[27][x][y] = H[x][y]

for x in range(31, 33):
    for y in range(13, 17):
        data_words[1][x][y] = H[x][y]

for x in range(31, 33):
    for y in range(9, 13):
        data_words[10][x][y] = H[x][y]
# 30
for x in range(29, 31):
    for y in range(29, 33):
        data_words[29][x][y] = H[x][y]

for x in range(29, 31):
    for y in range(25, 29):
        data_words[20][x][y] = H[x][y]

for x in range(29, 31):
    for y in range(21, 25):
        data_words[11][x][y] = H[x][y]

for x in range(29, 31):
    for y in range(17, 21):
        data_words[2][x][y] = H[x][y]

for x in range(29, 31):
    for y in range(13, 17):
        data_words[28][x][y] = H[x][y]

for x in range(29, 31):
    for y in range(9, 13):
        data_words[19][x][y] = H[x][y]
# 4
for x in range(27, 29):
    for y in range(29, 33):
        data_words[3][x][y] = H[x][y]

for x in range(27, 29):
    for y in range(20, 24):
        data_words[12][x][y] = H[x][y]

for x in range(27, 29):
    for y in range(16, 20):
        data_words[21][x][y] = H[x][y]

for x in range(27, 29):
    for y in range(12, 16):
        data_words[30][x][y] = H[x][y]

for x in range(27, 29):
    for y in range(9, 12):
        data_words[4][x][y] = H[x][y]

for x in range(25, 27):
    for y in range(9, 10):
        data_words[4][x][y] = H[x][y]
# 6
for x in range(25, 27):
    for y in range(10, 14):
        data_words[13][x][y] = H[x][y]

for x in range(25, 27):
    for y in range(14, 18):
        data_words[22][x][y] = H[x][y]

for x in range(25, 27):
    for y in range(18, 22):
        data_words[31][x][y] = H[x][y]

for x in range(25, 27):
    for y in range(22, 24):
        data_words[5][x][y] = H[x][y]

for x in range(25, 27):
    for y in range(29, 31):
        data_words[5][x][y] = H[x][y]
# 24
for x in range(23, 27):
    for y in range(31, 33):
        data_words[14][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(29, 31):
        data_words[23][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(25, 31):
        data_words[23][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(21, 25):
        data_words[32][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(20, 24):
        data_words[32][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(17, 21):
        data_words[6][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(16, 20):
        data_words[6][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(13, 17):
        data_words[15][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(12, 16):
        data_words[15][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(9, 13):
        data_words[24][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(8, 12):
        data_words[24][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(7, 8):
        data_words[33][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(7, 9):
        data_words[33][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(3, 6):
        data_words[33][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(4, 6):
        data_words[33][x][y] = H[x][y]

for x in range(23, 24):
    for y in range(0, 4):
        data_words[7][x][y] = H[x][y]

for x in range(24, 25):
    for y in range(0, 3):
        data_words[7][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(0, 1):
        data_words[7][x][y] = H[x][y]
# 17
for x in range(22, 23):
    for y in range(1, 5):
        data_words[16][x][y] = H[x][y]
for x in range(21, 22):
    for y in range(0, 4):
        data_words[16][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(4, 6):
        data_words[25][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(7, 9):
        data_words[25][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(5, 6):
        data_words[25][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(7, 10):
        data_words[25][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(10, 14):
        data_words[34][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(9, 13):
        data_words[34][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(14, 18):
        data_words[8][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(13, 17):
        data_words[8][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(18, 22):
        data_words[17][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(17, 21):
        data_words[17][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(22, 26):
        data_words[26][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(21, 25):
        data_words[26][x][y] = H[x][y]

for x in range(22, 23):
    for y in range(26, 30):
        data_words[35][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(25, 29):
        data_words[35][x][y] = H[x][y]
# ecc
for x in range(22, 23):
    for y in range(30, 33):
        ecc_words[0][x][y] = H[x][y]

for x in range(21, 22):
    for y in range(29, 33):
        ecc_words[0][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(32, 33):
        ecc_words[0][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(28, 32):
        ecc_words[16][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(29, 33):
        ecc_words[16][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(24, 28):
        ecc_words[32][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(25, 29):
        ecc_words[32][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(20, 24):
        ecc_words[48][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(21, 25):
        ecc_words[48][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(16, 20):
        ecc_words[1][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(17, 21):
        ecc_words[1][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(12, 16):
        ecc_words[17][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(13, 17):
        ecc_words[17][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(8, 12):
        ecc_words[33][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(9, 13):
        ecc_words[33][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(7, 8):
        ecc_words[49][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(7, 9):
        ecc_words[49][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(3, 6):
        ecc_words[49][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(4, 6):
        ecc_words[49][x][y] = H[x][y]

for x in range(19, 20):
    for y in range(0, 4):
        ecc_words[2][x][y] = H[x][y]

for x in range(20, 21):
    for y in range(0, 3):
        ecc_words[2][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(0, 1):
        ecc_words[2][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(1, 5):
        ecc_words[18][x][y] = H[x][y]
for x in range(17, 18):
    for y in range(0, 4):
        ecc_words[18][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(4, 6):
        ecc_words[34][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(7, 9):
        ecc_words[34][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(5, 6):
        ecc_words[34][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(7, 10):
        ecc_words[34][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(10, 14):
        ecc_words[50][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(9, 13):
        ecc_words[50][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(14, 18):
        ecc_words[3][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(13, 17):
        ecc_words[3][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(18, 22):
        ecc_words[19][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(17, 21):
        ecc_words[19][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(22, 26):
        ecc_words[35][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(21, 25):
        ecc_words[35][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(26, 30):
        ecc_words[51][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(25, 29):
        ecc_words[51][x][y] = H[x][y]

for x in range(18, 19):
    for y in range(30, 33):
        ecc_words[4][x][y] = H[x][y]

for x in range(17, 18):
    for y in range(29, 33):
        ecc_words[4][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(32, 33):
        ecc_words[4][x][y] = H[x][y]
# e21
for x in range(16, 17):
    for y in range(28, 32):
        ecc_words[20][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(29, 33):
        ecc_words[20][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(24, 28):
        ecc_words[36][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(25, 29):
        ecc_words[36][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(20, 24):
        ecc_words[52][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(21, 25):
        ecc_words[52][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(16, 20):
        ecc_words[5][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(17, 21):
        ecc_words[5][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(12, 16):
        ecc_words[21][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(13, 17):
        ecc_words[21][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(8, 12):
        ecc_words[37][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(9, 13):
        ecc_words[37][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(7, 8):
        ecc_words[53][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(7, 9):
        ecc_words[53][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(3, 6):
        ecc_words[53][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(4, 6):
        ecc_words[53][x][y] = H[x][y]

for x in range(15, 16):
    for y in range(0, 4):
        ecc_words[6][x][y] = H[x][y]

for x in range(16, 17):
    for y in range(0, 3):
        ecc_words[6][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(0, 1):
        ecc_words[6][x][y] = H[x][y]
# e23
for x in range(14, 15):
    for y in range(1, 5):
        ecc_words[22][x][y] = H[x][y]
for x in range(13, 14):
    for y in range(0, 4):
        ecc_words[22][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(4, 6):
        ecc_words[38][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(7, 9):
        ecc_words[38][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(5, 6):
        ecc_words[38][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(7, 10):
        ecc_words[38][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(10, 14):
        ecc_words[54][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(9, 13):
        ecc_words[54][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(14, 18):
        ecc_words[7][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(13, 17):
        ecc_words[7][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(18, 22):
        ecc_words[23][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(17, 21):
        ecc_words[23][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(22, 26):
        ecc_words[39][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(21, 25):
        ecc_words[39][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(26, 30):
        ecc_words[55][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(25, 29):
        ecc_words[55][x][y] = H[x][y]

for x in range(14, 15):
    for y in range(30, 33):
        ecc_words[8][x][y] = H[x][y]

for x in range(13, 14):
    for y in range(29, 33):
        ecc_words[8][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(32, 33):
        ecc_words[8][x][y] = H[x][y]
# e25
for x in range(12, 13):
    for y in range(28, 32):
        ecc_words[24][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(29, 33):
        ecc_words[24][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(24, 28):
        ecc_words[40][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(25, 29):
        ecc_words[40][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(20, 24):
        ecc_words[56][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(21, 25):
        ecc_words[56][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(16, 20):
        ecc_words[9][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(17, 21):
        ecc_words[9][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(12, 16):
        ecc_words[25][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(13, 17):
        ecc_words[25][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(8, 12):
        ecc_words[41][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(9, 13):
        ecc_words[41][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(7, 8):
        ecc_words[57][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(7, 9):
        ecc_words[57][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(3, 6):
        ecc_words[57][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(4, 6):
        ecc_words[57][x][y] = H[x][y]

for x in range(11, 12):
    for y in range(0, 4):
        ecc_words[10][x][y] = H[x][y]

for x in range(12, 13):
    for y in range(0, 3):
        ecc_words[10][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(0, 1):
        ecc_words[10][x][y] = H[x][y]
# e27
for x in range(10, 11):
    for y in range(1, 5):
        ecc_words[26][x][y] = H[x][y]
for x in range(9, 10):
    for y in range(0, 4):
        ecc_words[26][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(4, 6):
        ecc_words[42][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(7, 9):
        ecc_words[42][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(5, 6):
        ecc_words[42][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(7, 10):
        ecc_words[42][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(10, 14):
        ecc_words[58][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(9, 13):
        ecc_words[58][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(14, 18):
        ecc_words[11][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(13, 17):
        ecc_words[11][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(18, 22):
        ecc_words[27][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(17, 21):
        ecc_words[27][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(22, 26):
        ecc_words[43][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(21, 25):
        ecc_words[43][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(26, 30):
        ecc_words[59][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(25, 29):
        ecc_words[59][x][y] = H[x][y]

for x in range(10, 11):
    for y in range(30, 33):
        ecc_words[12][x][y] = H[x][y]

for x in range(9, 10):
    for y in range(29, 33):
        ecc_words[12][x][y] = H[x][y]

for x in range(8, 9):
    for y in range(24, 25):
        ecc_words[12][x][y] = H[x][y]
# e29
for x in range(8, 9):
    for y in range(20, 24):
        ecc_words[28][x][y] = H[x][y]
for x in range(7, 8):
    for y in range(21, 25):
        ecc_words[28][x][y] = H[x][y]

for x in range(8, 9):
    for y in range(16, 20):
        ecc_words[44][x][y] = H[x][y]
for x in range(7, 8):
    for y in range(17, 21):
        ecc_words[44][x][y] = H[x][y]

for x in range(8, 9):
    for y in range(12, 16):
        ecc_words[60][x][y] = H[x][y]
for x in range(7, 8):
    for y in range(13, 17):
        ecc_words[60][x][y] = H[x][y]

for x in range(8, 9):
    for y in range(9, 12):
        ecc_words[13][x][y] = H[x][y]
for x in range(7, 8):
    for y in range(9, 13):
        ecc_words[13][x][y] = H[x][y]

for x in range(5, 6):
    for y in range(9, 10):
        ecc_words[13][x][y] = H[x][y]
# e30
for x in range(5, 6):
    for y in range(10, 14):
        ecc_words[29][x][y] = H[x][y]

for x in range(4, 5):
    for y in range(9, 13):
        ecc_words[29][x][y] = H[x][y]

for x in range(5, 6):
    for y in range(14, 18):
        ecc_words[45][x][y] = H[x][y]

for x in range(4, 5):
    for y in range(13, 17):
        ecc_words[45][x][y] = H[x][y]

for x in range(5, 6):
    for y in range(18, 22):
        ecc_words[61][x][y] = H[x][y]

for x in range(4, 5):
    for y in range(17, 21):
        ecc_words[61][x][y] = H[x][y]

for x in range(5, 6):
    for y in range(22, 25):
        ecc_words[14][x][y] = H[x][y]

for x in range(4, 5):
    for y in range(21, 25):
        ecc_words[14][x][y] = H[x][y]

for x in range(3, 4):
    for y in range(24, 25):
        ecc_words[14][x][y] = H[x][y]
# e31
for x in range(3, 4):
    for y in range(20, 24):
        ecc_words[30][x][y] = H[x][y]
for x in range(2, 3):
    for y in range(21, 25):
        ecc_words[30][x][y] = H[x][y]

for x in range(3, 4):
    for y in range(16, 20):
        ecc_words[46][x][y] = H[x][y]
for x in range(2, 3):
    for y in range(17, 21):
        ecc_words[46][x][y] = H[x][y]

for x in range(3, 4):
    for y in range(12, 16):
        ecc_words[62][x][y] = H[x][y]
for x in range(2, 3):
    for y in range(13, 17):
        ecc_words[62][x][y] = H[x][y]

for x in range(3, 4):
    for y in range(9, 12):
        ecc_words[15][x][y] = H[x][y]
for x in range(2, 3):
    for y in range(9, 13):
        ecc_words[15][x][y] = H[x][y]

for x in range(1, 2):
    for y in range(9, 10):
        ecc_words[15][x][y] = H[x][y]
# e32

for x in range(1, 2):
    for y in range(10, 14):
        ecc_words[31][x][y] = H[x][y]

for x in range(0, 1):
    for y in range(9, 13):
        ecc_words[31][x][y] = H[x][y]

for x in range(1, 2):
    for y in range(14, 18):
        ecc_words[47][x][y] = H[x][y]

for x in range(0, 1):
    for y in range(13, 17):
        ecc_words[47][x][y] = H[x][y]
for x in range(1, 2):
    for y in range(18, 22):
        ecc_words[63][x][y] = H[x][y]

for x in range(0, 1):
    for y in range(17, 21):
        ecc_words[63][x][y] = H[x][y]

codewords = []
for _ in range(100):
    codeword = [["□" for _ in range(width)]
                for _ in range(height )]
    codewords.append(codeword)



for s in range(0, 9):
    for x in range(0, 33):
        for y in range(0, 33):
            if data_words[s][x][y] == "∎":
                block1[x][y] = data_words[s][x][y]
                codewords[s][x][y] = data_words[s][x][y]

for s in range(9, 18):
    for x in range(0, 33):
        for y in range(0, 33):
            if data_words[s][x][y] == "∎":
                block2[x][y] = data_words[s][x][y]
                codewords[s+25-9][x][y] = data_words[s][x][y]

for s in range(18, 27):
    for x in range(0, 33):
        for y in range(0, 33):
            if data_words[s][x][y] == "∎":
                block3[x][y] = data_words[s][x][y]
                codewords[s+50-18][x][y] = data_words[s][x][y]

for s in range(27, 36):
    for x in range(0, 33):
        for y in range(0, 33):
            if data_words[s][x][y] == "∎":
                block4[x][y] = data_words[s][x][y]
                codewords[s+75-27][x][y] = data_words[s][x][y]

for s in range(0, 16):
    for x in range(0, 33):
        for y in range(0, 33):
            if ecc_words[s][x][y] == "∎":
                block1[x][y] = ecc_words[s][x][y]
                codewords[s+9][x][y] = ecc_words[s][x][y]

for s in range(16, 32):
    for x in range(0, 33):
        for y in range(0, 33):
            if ecc_words[s][x][y] == "∎":
                block2[x][y] = ecc_words[s][x][y]
                codewords[s+9+25-16][x][y] = ecc_words[s][x][y]

for s in range(32, 48):
    for x in range(0, 33):
        for y in range(0, 33):
            if ecc_words[s][x][y] == "∎":
                block3[x][y] = ecc_words[s][x][y]
                codewords[s+9+50-32][x][y] = ecc_words[s][x][y]

for s in range(48, 64):
    for x in range(0, 33):
        for y in range(0, 33):
            if ecc_words[s][x][y] == "∎":
                block4[x][y] = ecc_words[s][x][y]
                codewords[s+9+75-48][x][y] = ecc_words[s][x][y]

blocks = [block1, block2, block3, block4]

for x in range(width):
    for y in range(height ):
        if block1[x][y] == "□" and block2[x][y] == "□" and block3[x][y] == "□" and block4[x][y] == "□":
            remainingblackmodule[x][y] = H[x][y]



codeword_counts = [(i, sum(sum(1 for cell in row if cell == "∎") for row in codeword)) for i, codeword in enumerate(codewords)]

codeword_counts_1_to_25 = [count for count in codeword_counts[:25]]

sorted_codeword_counts_1_to_25 = sorted(codeword_counts_1_to_25, key=lambda x: x[1])

codeword_counts_26_to_50 = [count for count in codeword_counts[25:50]]

sorted_codeword_counts_26_to_50 = sorted(codeword_counts_26_to_50, key=lambda x: x[1])

codeword_counts_51_to_75 = [count for count in codeword_counts[50:75]]

sorted_codeword_counts_51_to_75 = sorted(codeword_counts_51_to_75, key=lambda x: x[1])

codeword_counts_76_to_100 = [count for count in codeword_counts[75:100]]

sorted_codeword_counts_76_to_100 = sorted(codeword_counts_76_to_100, key=lambda x: x[1])

area1 = sorted_codeword_counts_1_to_25[-8:]
area2 = sorted_codeword_counts_26_to_50[-8:]
area3 = sorted_codeword_counts_51_to_75[-8:]
area4 = sorted_codeword_counts_76_to_100[-8:]
area5 = sorted_codeword_counts_1_to_25[:17]
area6 = sorted_codeword_counts_26_to_50[:17]
area7 = sorted_codeword_counts_51_to_75[:17]
area8 = sorted_codeword_counts_76_to_100[:17]

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
