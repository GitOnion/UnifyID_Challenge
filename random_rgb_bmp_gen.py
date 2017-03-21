from random_integer_gen import RandomIntGen
import png
import random


def random_png_gen(myemail, width, height):
    """
    Use the python built-in random module to reduce the usage of randor.org quota.
    (The quota has only 1mn bits, a single grey scale bmp pixel is 8 bits. if I am
    to generate 128 * 128 * 3 * 8 bits from random.org, two trials would drain it.)
    """
    rand_from_random_org = RandomIntGen(myemail).generate(256, 1, 255, 1, 10)
    pic = []
    for i in range(height):
        row = []
        for i in range(width):
            row += create_pixel(rand_from_random_org)
        pic.append(tuple(row))

    f = open('random.png', 'wb')
    w = png.Writer(128, 128)
    w.write(f, pic)
    f.close()

def create_pixel(randomList):
    pixel = []
    for i in range(3):
        color = random.sample(randomList,1)[0]
        color = (color + random.randint(0, 255)) % 255
        pixel.append(color)
    return pixel

if __name__ == "__main__":
    random_png_gen("myemail@gmail.com", 128, 128)
