print("Welcome to the tip calculator!")
bill_total = input ("What was the total bill? $")
tip_total = input("How much tip would you like to give? 10, 12, or 15? ")
people_total= input("How many people to split the bill? ")

floatbill = float(bill_total)
floattip = float(tip_total)
intpeople = int(people_total)

topay = (   (floatbill * (1 + (floattip / 100))) / intpeople      )


roundtopay = round(topay,2)

#in case the total only have one decimal, we use this format to place the "missing" cero
roundtopay = "{:.2f}".format(topay)
print(f"Each person should pay: ${roundtopay}")
