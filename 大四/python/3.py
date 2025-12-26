from PIL import Image
import random

qr_code_image = Image.open("qrcode.png")

qr_code_bw = qr_code_image.convert("1")

width, height = qr_code_bw.size

pixel_size = 10
n = 4
nb_H = 4
secret_H = [
    ["w" for _ in range(width // pixel_size)] for _ in range(height // pixel_size)
]

for x in range(0, width, pixel_size):
    for y in range(0, height, pixel_size):
        black_pixel_found = any(
            qr_code_bw.getpixel((x + i, y + j)) == 0
            for i in range(pixel_size)
            for j in range(pixel_size)
        )
        if black_pixel_found:
            secret_H[y // pixel_size][x // pixel_size] = "k"

for row in secret_H:
    print(" ".join(row))


def generate_Ql_regions(n, nb_H):
    Ql_regions = []

    if 2 <= n <= 2 * nb_H:
        # Case 1
        if n <= nb_H:
            for l in range(1, n + 1):
                Ql_region = generate_Ql_region(n, nb_H, l)
                Ql_regions.append(Ql_region)
        else:
            for l in range(1, n + 1):
                Ql_region = generate_Ql_region(n, nb_H, l)
                Ql_regions.append(Ql_region)

    elif n > 2 * nb_H:
        # Case 2
        for l in range(1, n + 1):
            Ql_region = generate_Ql_region(n, nb_H, l)
            Ql_regions.append(Ql_region)

    return Ql_regions


def generate_Ql_region(n, nb_H, l):
    if 2 <= n <= 2 * nb_H:
        if l <= nb_H:
            return generate_Ql_region_case1(n, nb_H, l)
        else:
            return generate_Ql_region_case2(n, nb_H, l)
    elif n > 2 * nb_H:
        return generate_Ql_region_case2(n, nb_H, l)


def generate_Ql_region_case1(n, nb_H, l):
    if l <= nb_H:
        # Sub-case 1:
        selected_blocks = random.sample(range(1, nb_H + 1), l)
        Ql_region = []
        for block in selected_blocks:
            Ql_region.extend(get_black_modules_in_block(block))
        return Ql_region
    else:
        # Sub-case 2:
        selected_blocks = random.sample(range(1, 2 * nb_H + 1), l - nb_H)
        Ql_region = []
        for block in selected_blocks:
            Ql_region.extend(get_black_modules_in_block(block))
        return Ql_region


def generate_Ql_region_case2(n, nb_H, l):
    selected_blocks = random.sample(range(1, 2 * nb_H + 1), n - 2 * nb_H)
    Ql_region = []
    for block in selected_blocks:
        Ql_region.extend(get_black_modules_in_block(block))
    return Ql_region


def get_black_modules_in_block(block):
    pass


Ql_regions = generate_Ql_regions(n, nb_H)


def generate_Q_hat_regions(n, nb_H):
    Q_hat_regions = []

    if n >= 2 * nb_H:
        for l in range(1, n + 1):
            Q_hat_region = generate_Q_hat_region(n, nb_H, l)
            Q_hat_regions.append(Q_hat_region)
    else:
        for l1 in range(1, nb_H + 1):
            Q_hat_region_l1 = generate_Q_hat_region(n, nb_H, l1)
            Q_hat_regions.append(Q_hat_region_l1)

        for l2 in range(nb_H + 1, 2 * nb_H + 1):
            Q_hat_region_l2 = generate_Q_hat_region(n, nb_H, l2)
            Q_hat_regions.append(Q_hat_region_l2)

    return Q_hat_regions


def generate_Q_hat_region(n, nb_H, l):
    if n >= 2 * nb_H:
        selected_blocks = random.sample(range(1, 2 * nb_H + 1), n - 2 * nb_H)
    else:
        if l <= nb_H:
            selected_blocks = [l]
        else:
            selected_blocks = []

    Q_hat_region = []
    for block in selected_blocks:
        Q_hat_region.extend(get_black_modules_in_block(block))

    return Q_hat_region


Q_hat_regions = generate_Q_hat_regions(n, nb_H)


def distribute_secret_to_shares(H, n, Q_hat_regions, Ql_regions):
    shares = []

    for i in range(n):
        share = generate_share_from_H(H, Q_hat_regions[i], Ql_regions[i])
        shares.append(share)

    return shares


def generate_share_from_H(H, Q_hat_region, Ql_region, pixel_size=10):
    share = []

    for x in range(len(H)):
        row = []
        for y in range(len(H[x])):
            if H[x][y] in Q_hat_region or H[x][y] in Ql_region:
                for i in range(pixel_size):
                    row.extend(["k"] * pixel_size)
            else:
                for i in range(pixel_size):
                    row.extend(["w"] * pixel_size)

        for i in range(pixel_size):
            share.append(row)

    return share


shares = distribute_secret_to_shares(secret_H, n, Q_hat_regions, Ql_regions)


def save_shares_as_images(shares):
    for i, share in enumerate(shares):
        image = create_image_from_share(share)
        filename = f"share_{i + 1}.png"  # You can specify the desired file format (e.g., .png, .jpg)
        image.save(filename)
        print(f"Share {i + 1} saved as {filename}")


def create_image_from_share(share):
    image = Image.new("1", (len(share[0]), len(share)), "white")
    pixels = image.load()

    for y in range(len(share)):
        for x in range(len(share[y])):
            if share[y][x] == "k":
                pixels[x, y] = 0  # Set the pixel to black

    return image


save_shares_as_images(shares)
