import PIL.Image

ASCII_CHARS = list(" .:-=+*#%@")

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def pixels_to_ascii(image):
    width = image.width
    pixels = list(image.getdata())
    lines = []

    for i in range(0, len(pixels), width):
        row_pixels = pixels[i:i+width]
        line = ""

        for r, g, b in row_pixels:
            gray = int(0.299*r + 0.587*g + 0.114*b)
            char = ASCII_CHARS[gray * (len(ASCII_CHARS) - 1) // 255]
            line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"

        lines.append(line)

    return "\n".join(lines)

def main(new_width=100):
    path = input("Enter a valid pathname to an image:\n")

    try:
        image = PIL.Image.open(path)
        image = image.convert("RGB")
    except:
        print(path, "is not a valid pathname to an image.")
        return

    new_image = resize_image(image)
    ascii_image = pixels_to_ascii(new_image)

    print(ascii_image)

if __name__ == "__main__":
    main()