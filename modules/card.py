class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        if suit == "Denari":
            short_suit = "D"
        elif suit == "Coppe":
            short_suit = "C"
        elif suit == "Spade":
            short_suit = "S"
        elif suit == "Bastoni":
            short_suit = "B"

        self.image_location = 'static/images/{}{}.png'.format(
            self.rank, self.short_suit)

    @property
    def image(self):
        return self.image_location