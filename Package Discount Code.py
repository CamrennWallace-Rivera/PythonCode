#camrenn wallace-rivera
#this program displays the price of a package from a software company w/wo discount

#data
package_price=99

#input by customer
quanity=float(input("how many packages did you purchase:"))

if quanity < 0:
        discount= 0
        print("there is no discount",'$',total)
if quanity < 10:
        discount = 0
elif quanity >= 10 and quanity <= 19:
        discount = .10 
elif quanity >= 20 and quanity <= 49:
        discount= .20 
elif quanity >= 50 and quanity <= 99:
        discount = .30
elif quanity >= 100:
        discount = .40

package_total=quanity*package_price
discount_amount=(package_total)*discount
total=package_total-discount

print("your total is:  $",total,'the precentage of discount recieved:  %',discount_amount)
    
