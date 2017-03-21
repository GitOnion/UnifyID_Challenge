from random_integer_gen import RandomIntGen
import png
import random


def random_png_gen(myemail="myemail@gmail.com"):
    """
    Use the python built-in random module to reduce the usage of randor.org quota.
    (The quota has only 1mn bits, a single grey scale bmp pixel is 8 bits. if I am
    to generate 128 * 128 * 3 * 8 bits from random.org, two trials would drain it.)
    """
    rand_from_random_org = RandomIntGen(myemail).generate(256, 1, 255, 1, 10)



    # f = open('random.png', 'wb')
    # w = png.Writer(128, 128)
    # w.write(f, pic)
    # f.close()

def 

if __name__ == "__main__":
    random_png_gen()
