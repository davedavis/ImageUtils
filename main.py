from PIL import Image, ImageDraw, ImageFont


def draw_letter(letter):
    """
        Generates a 312*512 image of a letter with the letter in the
        center. The image is saved as a png file.
        Arguments:
            letter: The letter to be drawn.
        """
    w, h = (512, 512)

    font = ImageFont.truetype("Arial_Bold.ttf", 600)

    im = Image.new("RGBA", (w, h), "white")
    draw = ImageDraw.Draw(im)
    draw.text((w / 2, h / 2), letter,
              font=font,
              anchor="mm",
              fill="#CFCECE")

    im.save(letter + ".png", "PNG")


def main():
    """
        The main function.
        Defines a list of characters and calls the draw_letter function
        to draw each character in a 512x512 image.
    """
    character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                      'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                      'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9']

    # For each letter in the char list, send it off to be drawn.
    for letter in character_list:
        draw_letter(letter)


if __name__ == '__main__':
    main()
