class student:
    def __init__(self , name , id , hight):
        self.name1 = name
        self.id1 = id
        self.hight1 = hight

    def showInfo(self):
        print(self.name1) 
        print(self.id1)
        print(self.hight1)

x = student("阿扁","10902188" ,168)
y = student("小英","10902558" ,164)
z = student("小馬", "10999855",177)
q = student("小韓", "19054886",175)
w = student("小柯", "10956688",173)

x.showInfo()
y.showInfo()
z.showInfo()
q.showInfo()
w.showInfo()