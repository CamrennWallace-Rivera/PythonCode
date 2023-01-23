
import random


def main():
    #local variables
    num1=0
    num2=0
    correctAnswer=0
    userAnswer=0

    #Get numbers

    num1=random.randint(1,999)
    num2=random.randint(1,999)

    #display math problem
    displayProblem(num1, num2)


    #get user answer 
    userAnswer=getAnswer()


    #calculate correct answer
    correctAnswer=num1+num2

    #display result 
    showResult(correctAnswer,userAnswer)
    
def displayProblem(num1,num2):
    print(num1)
    print("+",end='')
    print(num2)

def getAnswer():
    inputAnswer=int(input("Enter sum of numbers:  "))
    return inputAnswer

def showResult(correctAnswer,answer):
    if correctAnswer==answer:
        print("Correct answer – Good Work!")
    else:
         print("Incorrect... The correct answer is: ",correctAnswer)

main()
