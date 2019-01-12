class rev:
    def __init__(self,string):
        self.string=string
    def revers(self):
        rev=self.string.split()
        rev1=rev[-1::-1]
        rev2=' '.join(rev1)
        return rev2

def main():
    s=input("Enter the string:")
    a=rev(s)
    b=a.revers()
    print(b)

main()
