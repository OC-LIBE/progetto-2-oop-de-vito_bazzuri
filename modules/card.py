class Card:
    def __init__(self, rank, suit, flip = False):
        self.rank = rank
        self.suit = suit
        self.flip = flip

        if self.suit == "Denari":
            self.short_suit = "D"
        elif self.suit == "Coppe":
            self.short_suit = "C"
        elif self.suit == "Spade":
            self.short_suit = "S"
        elif self.suit == "Bastoni":
            self.short_suit = "B"

        if not self.flip:
            self.image_location = "static/images/{}{}.jpg".format(
                self.rank, self.short_suit)
        else:
            self.image_location = "static/images/RETRO.jpg"  
    
    def __str__(self):
        return f"{self.rank} di {self.suit}"
        
    @property
    def image(self):
        return self.image_location