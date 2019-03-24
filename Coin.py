import random


# Define your Coin class here
class Coin(object):
    """
    A class representing a Coin
    """

    def __init__(self):
        """
        Initialize the face of the coin
        """
        self.face = random.choice(["heads", "tails"])

    def get_face(self):
        """
        Get the face of the coin
        :return: the face of the coin
        """
        return self.face

    def flip(self):
        """
        Flip the coin assigning either heads or tails
        :return: None
        """
        self.face = random.choice(["heads", "tails"])


if __name__ == '__main__':
    """
    A program demonstrating the creation of Coin instance and calling class methods
    """
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
