class Card:
    def __init__(self, rank, suit, type,flip = False):
        #qua diciamo cosa serve per questo classe
        self.rank = rank
        self.suit = suit
        self.type = type
        self.flip = flip
        #qua diamo alle suits (i semi) delle abbreviazioni 
        if self.suit == "Denari" or self.suit == "Quadri":
            self.short_suit = "D"
        elif self.suit == "Coppe" or self.suit == "Fiori":
            self.short_suit = "C"
        elif self.suit == "Spade" or self.suit == "Picche":
            self.short_suit = "S"
        elif self.suit == "Bastoni" or self.suit == "Cuori":
            self.short_suit = "B"

        # Punti nell'essere presi e Forza nel prendere
        if self.rank == 1:
            self.point = 11
        elif self.rank == 3:
            self.point = 10
        elif self.rank == 10:
            self.point = 4
        elif self.rank == 9:
            self.point = 3
        elif self.rank == 8:
            self.point = 2
        else: # Da arrotondare verso il basso (0) per il conteggio dei punti
            self.point = self.rank/10
        
        self.image_set()

    def __str__(self):
        return f"{self.rank} di {self.suit}"
    
    def turn(self):
        #questa funzione serve per poi girare le carte del bot in modo che simuli una vera partita dove tu non conosci le carte del bot, dell'altro player
        self.flip = not self.flip # True to False, False to True
        self.image_set()
        return self
        
    def image_set(self):
        if not self.flip:#se la carta non la giri, facendo vedere il retro, allora si vede il seme e il numero della carta
            if self.type == 1:
                self.image_location = "static/images/{}{}.jpg".format( ##
                self.rank, self.short_suit)
            elif self.type == 2:
                self.image_location = "static/images2/{}{}.png".format( ##
                self.rank, self.short_suit)
        else:
            self.image_location = "static/images/RETRO.png"  

    @property
    def image(self):
        return self.image_location