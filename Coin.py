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


if __name__ == '__main__':
    # put your code that utilizes your Coin class here
    pass
  
