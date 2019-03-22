import random


# Define your Coin class here
class Coin(object):

    def __init__(self):
        self.face = random.choice(["heads", "tails"])

    def get_face(self):
        return self.face

    def flip(self):
        self.face = random.choice(["heads", "tails"])



if __name__ == '__main__':
    # put your code that utilizes your Coin class here
    Coin1 = Coin()
    num_heads = 0
    num_tails = 0
    for i in range(1000):
        if Coin1.get_face() == "heads":
            num_heads += 1
        elif Coin1.get_face() == "tails":
            num_tails += 1
        Coin1.flip()

    print("The number of head flips is", num_heads)
    print("The number of tail flips is", num_tails)
    pass
#
