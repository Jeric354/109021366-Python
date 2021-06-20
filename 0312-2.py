class Chess:
    def __init__(self, word ,color ,play):
        self.word1  =word
        self.color1 =color
        self.play1 = play

    def showInfo(self):
        print(self.word1)
        print(self.color1)
        print(self.play1)

x = Chess("象","red","前後左右吃")
y = Chess("炮","red","隔著吃")    
z = Chess("帥","red","最大")   

x.showInfo()
y.showInfo()
z.showInfo()
