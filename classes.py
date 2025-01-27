class Cat:
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs

    def __str__(self):
        return self.color+":"+str(self.legs)            

felix = Cat("ginger",4)
rover = Cat("black",4)
stumpy = Cat("white",4)

print(felix,rover,stumpy)