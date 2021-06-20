class Hero:
    def __init__(self, name, id , hight ,weight ,cp):
        self.name1 = name
        self.id1 = id
        self.hight1 = hight
        self.weight1 = weight
        self.cp1 = cp 
    
    def showInfo(self):
        print(self.name1)
        print(self.id1)
        print(self.hight1)
        print(self.weight1)
        print(self.cp1)

x  = Hero("大葛葛","01",185 ,85 ,10000)
x1 = Hero("大姊姊","02",160 ,45 ,5000)
x2 = Hero("小底底","03",158 ,35 ,3000)

x.showInfo()
x1.showInfo()
x2.showInfo()