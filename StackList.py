#Algo2
#STACK USING PYTHON-- list
#LIFO TOP-->lst[-1]
#PUSH POP ISEMPTY ISFULL DISPLAY
class Stack:
    def __init__(self,stacklst):
        self.stacklst=stacklst
        self.top=self.stacklst[-1]
    def __str__(self):
        return f"\nList:: {self.stacklst}.\nTop:: {self.top}"
    def push(self,item):
        self.stacklst.append(item)
        self.top=self.stacklst[-1]
        return f"{self.top} is pushed to the stack."

    def pop(self):
        if self.stacklst==[]:
            return "Underflow.List is empty!"
        else:
            self.top=self.stacklst[-2]
            popped=self.stacklst.pop()
            return f"{popped} is popped."

    def display(self):
        print("\nFollowing is the stack:")
        for x in self.stacklst:
            print(x,end="")
            print(" ",end="")
        print()
    
#Taking user input
lst=[]
inputlist=input("Enter the list:")
list1=inputlist.split()
for x in list1:
    element=int(x)
    lst.append(element)

#Object for stack class
Stack1=Stack(lst)

#Performing Operations According to user's choices
ch=True
while ch:
    print("\n\n****Choose one of the options:\n1.Push Operation\n2.Pop Operation\n3.Display Operation\n4.Printing infomation\n5.Exit****")
    ch=int(input("Enter a no. among 1, 2, 3, 4 or 5:"))

    if ch not in [1,2,3,4,5]:
        print("\n\nOops! Remember Number should be 1, 2 ,3, 4 or 5")
        print("Choose one of the options:\n1.Push Operation\n2.Pop Operation\n3.Display Operation\n4.Printing informtion\n5.Exit")
        ch=int(input("Enter a no. among 1, 2, 3, 4 or 5:"))
    
    if ch==1:
        item=int(input("Enter the no. to be inserted:"))
        print("\n"+Stack1.push(item))

    elif ch==2:
        print("\n"+Stack1.pop())

    elif ch==3:
        Stack1.display()

    elif ch==4:
        print(Stack1)

    elif ch==5:
        break

print("\n\n***Program has terminated.***")
