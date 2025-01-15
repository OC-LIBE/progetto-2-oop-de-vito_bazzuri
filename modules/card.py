class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        if self.suit == "Denari":
            self.short_suit = "D"
        elif self.suit == "Coppe":
            self.short_suit = "C"
        elif self.suit == "Spade":
            self.short_suit = "S"
        elif self.suit == "Bastoni":
            self.short_suit = "B"

        if rank != 0:
            self.image_location = "static/images/{}{}.jpg".format(
                self.rank, self.short_suit)
        else:
            self.image_location = "static/images/RETRO.jpg"  
        
    @property
    def image(self):
        return self.image_location