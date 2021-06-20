class book:
    def __init__(self, name , author , year):
        self.name1 = name
        self.author1 = author
        self.year1 = year

    def showInfo(self):
        print(self.name1)
        print(self.author1)
        print(self.year1)

x = book("Harry Potter1","JK Rolling",1997)
y = book("Harry Potter2","JK Rolling",1998)
z = book("Harry Potter3","JK Rolling",1999)
q = book("Harry Potter4","JK Rolling",2000)
w = book("Harry Potter5","JK Rolling",2003)

x.showInfo()
y.showInfo()
z.showInfo()
q.showInfo()
w.showInfo()