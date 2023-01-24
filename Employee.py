#this program is to practice the use of classes and implement functions
#and recall them in the main method.
#the program uses the data in a pre exisiting .txt file 
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        self.bonus=0

    def getPay(self):
        return self.pay

    def setPay(self,pay):
        self.pay=pay

    def setBonus(self,Bonus):
        self.Bonus=Bonus

    def getBonus(self):
        return self.Bonus

     
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
       

    def __str__(self):
       
       return 'Employee name: '+self.fullName()+' Employee pay: ' +str(self.pay)

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def print_queue(self):
        for item in self.items:
            print(item, end=" ")
        print()
       


def main():

    q=Queue()
    
    file=open("dirany.txt","r+")

    for line in file.readlines():

        fLine=line.strip().split("\t")

        employee=Employee(fLine[0],fLine[1],fLine[2])

        q.enqueue(employee)

    q.print_queue()

    employees=[]

    count=0

    while not q.is_empty():

        e=q.dequeue()
        
        employees.append(calculateBonus(e,20-count))

        count+=1
        

        
def calculateBonus(employee,num):

    bonus=employee.pay*int((20-num)/100)

    employee.setBonus(bonus)

    return employee

    q.enqueue()

    print(q)




main()
        

    

