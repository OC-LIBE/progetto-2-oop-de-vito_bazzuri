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

        # Punti nell'essere presi e Forza nel prendere
        if self.rank == 1:
            self.points == 11
        elif self.rank == 3:
            self.points == 10
        if self.rank == 10:
            self.points == 4
        elif self.rank == 9:
            self.points == 3
        elif self.rank == 8:
            self.points == 2
        else: # Da arrotondare verso il basso (0) per il conteggio dei punti
            self.point = self.rank/10
        
        self.image_set()

    def __str__(self):
        return f"{self.rank} di {self.suit}"
    
    def turn(self):
        self.flip = not self.flip # True to False, False to True
        self.image_set()
        return self
        
    def image_set(self):
        if not self.flip:
            self.image_location = "static/images/{}{}.jpg".format(
            self.rank, self.short_suit)
        else:
            self.image_location = "static/images/RETRO.png"  

    @property
    def image(self):
        return self.image_location
    
    @property
    def strenght(self):
        
        return self.points
    
    @property
    def points(self):
        
        return self.points