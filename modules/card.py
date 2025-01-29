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
<<<<<<< Updated upstream
            self.image_location = "static/images/RETRO.jpg"
        
=======
            self.image_location = "static/images/RETRO.jpg"  
    
    def points(self):
        if self.rank == 2 or 4 or 5 or 6 or 7:
            self.points == 0
        elif self.rank == 8 :
            self.points == 2
        elif self.rank == 9:
            self.points == 3
        elif self.rank == 10:
            self.points == 4
        elif self.rank == 3:
            self.points == 10 
        else: 
            self.points == 11

>>>>>>> Stashed changes
    def __str__(self):
        return f"{self.rank} di {self.suit}"
    
    def hide(self):
        self.flip = True
        return self

    def show(self):
        self.flip = False
        return self
        
    @property
    def image(self):
        return self.image_location