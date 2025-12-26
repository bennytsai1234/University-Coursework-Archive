from PIL import Image
import random

qr_code_image = Image.open("qrcode.png")

qr_code_bw = qr_code_image.convert("1")

width, height = qr_code_bw.size

pixel_size = 10

Hwidth = width // pixel_size
n = 3
nb_H = 3
H = [["□" for _ in range(Hwidth)] for _ in range(height // pixel_size)]

for x in range(0, width, pixel_size):
    for y in range(0, height, pixel_size):
        black_pixel_found = any(
            qr_code_bw.getpixel((x + i, y + j)) == 0
            for i in range(pixel_size)
            for j in range(pixel_size)
        )
        if black_pixel_found:
            H[y // pixel_size][x // pixel_size] = "∎"


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
# 複製 H到對應位置
for x in range(21, 25):
    for y in range(9, 25):
        block1[y][x] = H[y][x]

for x in range(19, 21):
    for y in range(21, 25):
        block1[y][x] = H[y][x]

for x in range(17, 19):
    for y in range(9, 10):
        block1[y][x] = H[y][x]

for x in range(19, 21):
    for y in range(9, 16):
        block1[y][x] = H[y][x]

for x in range(11, 12):
    for y in range(12, 13):
        block1[y][x] = H[y][x]

for x in range(9, 13):
    for y in range(0, 6):
        block1[y][x] = H[y][x]

for x in range(9, 13):
    for y in range(7, 12):
        block1[y][x] = H[y][x]

for x in range(9, 11):
    for y in range(12, 25):
        block1[y][x] = H[y][x]

for x in range(7, 9):
    for y in range(9, 17):
        block1[y][x] = H[y][x]

for x in range(0, 6):
    for y in range(9, 17):
        block1[y][x] = H[y][x]


for x in range(17, 19):
    for y in range(10, 16):
        block2[y][x] = H[y][x]

for x in range(17, 19):
    for y in range(21, 25):
        block2[y][x] = H[y][x]

for x in range(15, 17):
    for y in range(21, 25):
        block2[y][x] = H[y][x]

for x in range(15, 16):
    for y in range(17, 21):
        block2[y][x] = H[y][x]

for x in range(15, 17):
    for y in range(13, 16):
        block2[y][x] = H[y][x]

for x in range(14, 15):
    for y in range(13, 14):
        block2[y][x] = H[y][x]

for x in range(13, 17):
    for y in range(7, 13):
        block2[y][x] = H[y][x]

for x in range(13, 17):
    for y in range(0, 6):
        block2[y][x] = H[y][x]


for x in range(13, 14):
    for y in range(13, 14):
        block3[y][x] = H[y][x]

for x in range(13, 15):
    for y in range(14, 25):
        block3[y][x] = H[y][x]

for x in range(11, 13):
    for y in range(13, 25):
        block3[y][x] = H[y][x]

for x in range(12, 13):
    for y in range(12, 13):
        block3[y][x] = H[y][x]


for x in range(Hwidth):
    for y in range(height // pixel_size):
        if block1[y][x] == "□" and block2[y][x] == "□" and block3[y][x] == "□":
            remainingblackmodule[y][x] = H[y][x]

blocks = [block1, block2, block3, block4]

def generate_Ql_regions(n, nb_H):
    Ql_regions = []

    if 2 <= n <= 2 * nb_H:
        # Case 1
        if n <= nb_H:
            selected_blocks = random.sample(blocks, n)
            unselected_blocks = [
                block for block in blocks if block not in selected_blocks
            ]
            for l in range(1, n + 1):
                Ql_region = generate_Ql_region(
                    n, nb_H, l, selected_blocks, unselected_blocks
                )
                Ql_regions.append(Ql_region)
        else:
            selected_blocks = random.sample(blocks, (2*nb_H-n))
            unselected_blocks = [
                block for block in blocks if block not in selected_blocks
            ]
            Ql2_list = []
            Ql2_region = generate_Ql_region(
                n, nb_H, n-(2*nb_H-n)+1, selected_blocks, unselected_blocks
            )
            for l2 in range(1, n-(2*nb_H-n)+1):
                Ql2_item = [["□" for _ in range(Hwidth)]
                            for _ in range(height // pixel_size)]
                Ql2_list.append(Ql2_item)

            for x in range(0, Hwidth):
                for y in range(0, Hwidth):
                    if Ql2_region[y][x] == "∎":
                        random_number = random.randint(0, n-(2*nb_H-n)-1)
                        selected_Ql2 = Ql2_list[random_number]
                        selected_Ql2[y][x] = Ql2_region[y][x]
            for Ql2_item in Ql2_list:
                Ql_regions.append(Ql2_item)
            for l in range(1, (2*nb_H-n)+1):
                Ql_region = generate_Ql_region(
                    n, nb_H, l, selected_blocks, unselected_blocks
                )
                Ql_regions.append(Ql_region)

    elif n > 2 * nb_H:
        # Case 2
        selected_blocks = random.sample(blocks, n)
        unselected_blocks = [
            block for block in blocks if block not in selected_blocks
        ]
        for l in range(1, n + 1):
            Ql_region = generate_Ql_region(n, nb_H, l)
            Ql_regions.append(Ql_region)

    return Ql_regions


def generate_Ql_region(n, nb_H, l, selected_blocks, unselected_blocks):
    if 2 <= n <= 2 * nb_H:
        if n <= nb_H:
            return generate_Ql_region_case1(
                n, nb_H, l, selected_blocks, unselected_blocks
            )
        else:
            return generate_Ql_region_case1(n, nb_H, l, selected_blocks, unselected_blocks)
    elif n > 2 * nb_H:
        return generate_Ql_region_case2(n, nb_H, l, selected_blocks, unselected_blocks)


def generate_Ql_region_case1(n, nb_H, l, selected_blocks, unselected_blocks):
    if n <= nb_H:
        block = selected_blocks[l-1]
        Ql_region = [
            ["□" for _ in range(Hwidth)]
            for _ in range(height // pixel_size)
        ]
        for x in range(0, Hwidth):
            for y in range(0, Hwidth):
                if block[y][x] == "∎":
                    Ql_region[y][x] = block[y][x]
        if l == n:
            for block in unselected_blocks:
                for x in range(0, Hwidth):
                    for y in range(0, Hwidth):
                        if block[y][x] == "∎":
                            Ql_region[y][x] = block[y][x]
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
                        if block[y][x] == "∎":
                            Ql_region[y][x] = block[y][x]
        else:
            block = selected_blocks[l-1]
            Ql_region = [
                ["□" for _ in range(Hwidth)]
                for _ in range(height // pixel_size)
            ]
            for x in range(0, Hwidth):
                for y in range(0, Hwidth):
                    if block[y][x] == "∎":
                        Ql_region[y][x] = block[y][x]
        return Ql_region


def generate_Ql_region_case2(n, nb_H, l, selected_blocks, unselected_blocks):
    selected_blocks = random.sample(range(1, 2 * nb_H + 1), n - 2 * nb_H)
    Ql_region = []
    for block in selected_blocks:
        Ql_region.extend()
    return Ql_region


Ql_regions = generate_Ql_regions(n, nb_H)
nQ = 0
for x in range(0, Hwidth):
    for y in range(0, Hwidth):
        if remainingblackmodule[y][x] == "∎":
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
            x = random.randint(0, 24)
            y = random.randint(0, 24)

            if remainingblackmodule[y][x] == "∎" and (x, y) not in selected_points:
                Q_hat_region[y][x] = remainingblackmodule[y][x]
                remainingblackmodule[y][x] = "□"
                selected_points.append((x, y))
                C -= 1
        if l == n:
            for x in range(0, Hwidth):
                for y in range(0, Hwidth):
                    if remainingblackmodule[y][x] == "∎":
                        Q_hat_region[y][x] = remainingblackmodule[y][x]
    else:
        pass

    return Q_hat_region


Q_hat_regions = generate_Q_hat_regions(n, nQ)
for index, Q_hat_region in enumerate(Q_hat_regions):
    print(f"Q_hat_region {index + 1}:")
    for row in Q_hat_region:
        print(" ".join(row))
    print("\n")


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


for i in range(1, n+1):
    print(f"Ql_regions[{i}]:")
    for row in Ql_regions[i - 1]:
        print(" ".join(row))
    print("\n")

shares = distribute_secret_to_shares(H, n, Q_hat_regions, Ql_regions)


def save_shares_as_images(shares):
    for i, share in enumerate(shares):
        image = create_image_from_share(share)
        # You can specify the desired file format (e.g., .png, .jpg)
        filename = f"share_{i + 1}.png"
        image.save(filename)
        print(f"Share {i + 1} saved as {filename}")


def create_image_from_share(share):
    image = Image.new("1", (len(share[0]), len(share)), "white")
    pixels = image.load()

    for y in range(len(share)):
        for x in range(len(share[y])):
            if share[y][x] == "∎":
                pixels[x, y] = 0
    return image


save_shares_as_images(shares)
