class less:
    def __init__(self,lst):
        self.lst=lst
    def lesser(self):
        a=[i for i in self.lst if i<5]
        return a
def main():
    n=int(input('Enter:'))
    lst=[int(input()) for i in range(n)]
    a=less(lst)
    b=a.lesser()
    print(b)

main()
