#farmer increase is 10% per month
#ask the farmer to insert current no. of chickens he has and 
#the no. of months he would like his chicken count.
#output estimated chicken count

#declear variables
increasePerMonth = 10 #percent
getCurrentCountOfChicken = 0
getPredictedMonthCount = 0

getCurrentCountOfChicken  = int(input("Kindly enter the current count of chicken: "))
getPredictedMonthCount = int(input("Kindly enter number of month to predict count: "))

calPercent = ((getCurrentCountOfChicken * 10) / 100 ) + getCurrentCountOfChicken
totalEstimate = calPercent * getPredictedMonthCount

print("Your estimated count of chicken for " + str(getPredictedMonthCount) + "month is:" + str(totalEstimate))