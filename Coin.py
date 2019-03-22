import random


# Define your Coin class here
class Coin(object):

    def __init__(self):
        Coin.face = random.randint(1, 2)

    def get_face(self):
        if self.face == 1:
            return "heads"
        else:
            return "tails"

    def flip(self):
        Coin.face = random.randint(1, 2)


def main():
    Coin1 = Coin()
    num_heads = 0
    num_tails = 0
    for i in range(1000):
        if Coin1.get_face() == "heads":
            num_heads += 1
        else:
            num_tails += 1
        Coin1.flip()

    print("The number of head flips is", num_heads)
    print("The number of tail flips is", num_tails)


main()
# if __name__ == '__main__':
#     # put your code that utilizes your Coin class here
#     pass
#
