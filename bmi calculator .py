#this program will display the users BMI indicating if whom is optimal weight,over wieght, under weight

#equation
weight=int(input("enter your weight in pounds:"))
height=float(input("enter your height in inches:"))
BMI=weight*703/(height)**2
if BMI <= 18.5:
      print(" You're Underweight","Your BMI is:", BMI)
elif BMI > 18.5 and BMI > 25:
         print("Youre Optimal in weight ",'Your BMI is:',BMI)
elif BMI > 25 and BMI < 30:
              print(' Youre Overwight', 'Your BMI is:',BMI)
else:
    print("Obesity")
           

