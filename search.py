class Search:
    def __init__(self,lst,search):
        self.lst=lst
        self.search=search
    def sear(self):
        searchList=[]
        x=-1
        for i in self.lst:
            x=x+1
            if self.search==i:
                searchList.append(x)
        return searchList
    
def main():
    num=int(input("Enter the number of elements in the list"))
    lst=[int(input()) for i in range(num)]
    search=int(input("Enter search element"))
    a=Search(lst,search)
    b=a.sear()
    print(b)

main()
            
