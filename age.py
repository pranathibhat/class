import datetime
now=datetime.datetime.now()
class People:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def turning(self):
        self.more=100-self.age
        self.years=now.year+self.more
        print("Hey %s! You'll turn 100 years old in %d"%(self.name,self.years))

x=People("Sandy",32)
x.turning()
    
