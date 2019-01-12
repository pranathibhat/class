class user:
    
    def update(self):

        self.n=int(input("Enter no.:"))
        self.d={}
        for i in range(self.n):
            self.name=input("Enter the name:")
            self.usn=input("Enter usn:")
            if self.usn in self.d.keys():
                print("Already present in dictionary")
            else:
                self.d.update({self.usn:self.name})
                self.d[self.usn]=self.name
        return self.d

a=user()
b=a.update()
print(b)
