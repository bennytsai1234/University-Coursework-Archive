from PIL import Image
import random
#test
#7+6+6+6
qr_code_image = Image.open("qrcode.png")

qr_code_bw = qr_code_image.convert("1")

width, height = qr_code_bw.size

pixel_size = 10

Hwidth = width // pixel_size
n = 1
nb_H = 4
H = [["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)]
for x in range(0, width, pixel_size):
    for y in range(0, height, pixel_size):
        black_pixel_found = any(
            qr_code_bw.getpixel((x + i, y + j)) == 0
            for i in range(pixel_size)
            for j in range(pixel_size)
        )
        if black_pixel_found:
            H[x // pixel_size][y // pixel_size] = "∎"


# 定義 block
block1 = [
    ["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)
]
block2 = [
    ["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)
]
block3 = [
    ["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)
]
block4 = [
    ["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)
]
remainingblackmodule = [
    ["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)
]

# 定義 block data
data_words = []
ecc_words = []
for _ in range(36):
    data_word = [["□" for _ in range(Hwidth)]
                 for _ in range(height // pixel_size)]
    data_words.append(data_word)

for _ in range(64):
    ecc_word = [["□" for _ in range(Hwidth)]
                for _ in range(height // pixel_size)]
    ecc_words.append(ecc_word)
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
    codeword = [["□" for _ in range(Hwidth)]
                for _ in range(height // pixel_size)]
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

for x in range(Hwidth):
    for y in range(height // pixel_size):
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

area1 = sorted_codeword_counts_1_to_25[7:13]
area2 = sorted_codeword_counts_1_to_25[13:19]
area3 = sorted_codeword_counts_1_to_25[19:25]
area4 = sorted_codeword_counts_26_to_50[7:13]
area5 = sorted_codeword_counts_26_to_50[13:19]
area6 = sorted_codeword_counts_26_to_50[19:25]
area7 = sorted_codeword_counts_51_to_75[7:13]
area8 = sorted_codeword_counts_51_to_75[13:19]
area9 = sorted_codeword_counts_51_to_75[19:25]
area10= sorted_codeword_counts_76_to_100[7:13]
area11= sorted_codeword_counts_76_to_100[13:19]
area12= sorted_codeword_counts_76_to_100[19:25]



areas = [area1, area2, area3, area4, area5, area6, area7, area8,area9, area10, area11,area12]

area1_first_element = area1[0][1]
area2_first_element = area2[0][1]
area3_first_element = area3[0][1]
area4_first_element = area4[0][1]
area5_first_element = area5[0][1]
area6_first_element = area6[0][1]
area7_first_element = area7[0][1]
area8_first_element = area8[0][1]
area9_first_element = area9[0][1]
area10_first_element = area10[0][1]
area11_first_element = area11[0][1]
area12_first_element = area12[0][1]
first_elements = []

first_elements.append(area1_first_element)
first_elements.append(area2_first_element)
first_elements.append(area3_first_element)
first_elements.append(area4_first_element)
first_elements.append(area5_first_element)
first_elements.append(area6_first_element)
first_elements.append(area7_first_element)
first_elements.append(area8_first_element)
first_elements.append(area9_first_element)
first_elements.append(area10_first_element)
first_elements.append(area11_first_element)
first_elements.append(area12_first_element)
for element in first_elements:
    print(element)

def generate_Ql_regions(n, nb_H):
    Ql_regions = []
    mn = 0
    c=7
    for l in range(0, 1):
        Ql_region = [["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)]
        for z in range(0,11):
            for word_index,count in areas[z]:
                for x in range(0, Hwidth):
                    for y in range(0, Hwidth):
                        if codewords[word_index][x][y] == "∎":
                            Ql_region[x][y] = codewords[word_index][x][y]
    for word_index,count in areas[11]:
        for x in range(0, Hwidth):
            for y in range(0, Hwidth):
                if codewords[word_index][x][y] == "∎":
                    Ql_region[x][y] = codewords[word_index][x][y]
                    mn += 1
                if mn==c:
                    break
            if mn==c:
                break  
        mn =0                 
        
    
    Ql_regions.append(Ql_region)
    return Ql_regions



def generate_Ql_region_case1(n, nb_H, l, selected_blocks, unselected_blocks):
    if n <= nb_H:
        block = selected_blocks[l-1]
        Ql_region = [
            ["□" for _ in range(Hwidth)]
            for _ in range(height // pixel_size)
        ]
        for x in range(0, Hwidth):
            for y in range(0, Hwidth):
                if block[x][y] == "∎":
                    Ql_region[x][y] = block[x][y]
        if l == n:
            for block in unselected_blocks:
                for x in range(0, Hwidth):
                    for y in range(0, Hwidth):
                        if block[x][y] == "∎":
                            Ql_region[x][y] = block[x][y]
        return Ql_region
    else:
        # Sub-case 2:
        if l > 2*nb_H-n:
            Ql_region = [
                ["□" for _ in range(Hwidth)]
                for _ in range(height // pixel_size)
            ]
            for block in unselected_blocks:
                for x in range(0, Hwidth):
                    for y in range(0, Hwidth):
                        if block[x][y] == "∎":
                            Ql_region[x][y] = block[x][y]
        else:
            block = selected_blocks[l-1]
            Ql_region = [
                ["□" for _ in range(Hwidth)]
                for _ in range(height // pixel_size)
            ]
            for x in range(0, Hwidth):
                for y in range(0, Hwidth):
                    if block[x][y] == "∎":
                        Ql_region[x][y] = block[x][y]
        return Ql_region


Ql_regions = generate_Ql_regions(n, nb_H)



nQ = 0
for x in range(0, Hwidth):
    for y in range(0, Hwidth):
        if remainingblackmodule[x][y] == "∎":
            nQ = nQ+1
f = (nQ//n)


def generate_Q_hat_regions(n, nQ):
    Q_hat_regions = []

    if n < nQ:
        for l in range(1, n + 1):
            Q_hat_region = generate_Q_hat_region(n, nQ, l)
            Q_hat_regions.append(Q_hat_region)
    else:
        for l1 in range(1,  nQ + 1):
            Q_hat_region_l1 = generate_Q_hat_region(n, nQ, l1)
            Q_hat_regions.append(Q_hat_region_l1)

        for l2 in range(nQ + 1, n + 1):
            Q_hat_region_l2 = generate_Q_hat_region(n, nQ, l2)
            Q_hat_regions.append(Q_hat_region_l2)

    return Q_hat_regions


def generate_Q_hat_region(n, nQ, l):
    if n < nQ:
        Q_hat_region = [["□" for _ in range(Hwidth)]
                        for _ in range(height // pixel_size)
                        ]
        C = f
        selected_points = []
        while C > 0:
            x = random.randint(0, 32)
            y = random.randint(0, 32)

            if remainingblackmodule[x][y] == "∎" and (x, y) not in selected_points:
                Q_hat_region[x][y] = remainingblackmodule[x][y]
                remainingblackmodule[x][y] = "□"
                selected_points.append((x, y))
                C -= 1
        if l == n:
            for x in range(0, Hwidth):
                for y in range(0, Hwidth):
                    if remainingblackmodule[x][y] == "∎":
                        Q_hat_region[x][y] = remainingblackmodule[x][y]
    else:
        pass

    return Q_hat_region


Q_hat_regions = generate_Q_hat_regions(n, nQ)




def distribute_secret_to_shares(H, n, Q_hat_regions, Ql_regions):
    shares = []

    for i in range(n):
        share = generate_share_from_H(H, Q_hat_regions[i], Ql_regions[i])
        shares.append(share)

    return shares


def generate_share_from_H(H, Q_hat_region, Ql_region, pixel_size=10):
    share = []
    for x in range(0, Hwidth):
        row = []
        for y in range(0, Hwidth):
            if H[x][y] == Q_hat_region[x][y] == "∎" or H[x][y] == Ql_region[x][y] == "∎":
                for i in range(pixel_size):
                    row.extend(["∎"])
            else:
                for i in range(pixel_size):
                    row.extend(["□"])
        for i in range(pixel_size):
            share.append(row)

    return share



shares = distribute_secret_to_shares(H, n, Q_hat_regions, Ql_regions)


def save_shares_as_images(shares):
    for i, share in enumerate(shares):
        image = create_image_from_share(share)
        filename = f"merged_image.png"
        image.save(filename)


def create_image_from_share(share):
    image = Image.new("1", (len(share[0]), len(share)), "white")
    pixels = image.load()

    for y in range(len(share)):
        for x in range(len(share[y])):
            if share[x][y] == "∎":
                pixels[x, y] = 0
    return image


save_shares_as_images(shares)
