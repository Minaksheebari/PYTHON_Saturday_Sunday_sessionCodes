# Simple interest calculation 

# A = P(1+rt)
# A = final amount #this should be the output
# P = initial principal balance #input from user
# r = annual interest rate #fixed variable value eg 5%
# t = time (in years) #input from user

# stage 1 - you are taking the inputes and it will display the final amount
# stage 2 - validations for 1) zero input 

principalAmount = int(input("Enter Principal Amount to calculate Interest: "))
if(principalAmount<=0):                                #stage 2
    print("Zero and negative values are not acceptable!")
    principalAmount = int(input("Enter Principal Amount to calculate Interest: "))

rateOfInterest = 5   #we can use 0.05 and skip divide by 100 in calculation

timePeriod = int(input("Enter time in years: "))
if(timePeriod<=0):
    print("Zero and negative values are not acceptable!")
    timePeriod = int(input("Enter time in years: "))

totalAmount = principalAmount * (1 + rateOfInterest/100*timePeriod)

print("Total Amount is: ", totalAmount)     #stage 1 