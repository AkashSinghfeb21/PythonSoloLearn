class Player:
    def __init__(self,name,lives):
        self.name = name
        self._lives = lives

    def hit(self):
        if(self._lives>0):
            self._lives -= 1
            print(f"{self.name} has {self._lives} lives left.")   
        elif(self._lives==0):
            print("Game Over")    

p = Player("John",3)
p.hit()
p.hit()
p.hit()
p.hit()