class Dup:
    def __init__(self,dup):
        self.dup=dup
    def remove(self):
        final_list=[]
        for num in self.dup:
            if num not in final_list:
                final_list.append(num)
        return final_list

def main():
    n=int(input("Enter number of items in list"))
    dup=[input() for i in range(n)]
    a=Dup(dup)
    b=a.remove()
    print("New list is:")
    print(b)

main()
