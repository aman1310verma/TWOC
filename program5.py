#taking input
p1= eval(input("Enter details of player 1"))
p2= eval(input("Enter details of player 2"))
p3= eval(input("Enter details of player 3"))


strike1= p1/60*100
strike2= p2/60*100
strike3= p3/60*100

print("strike rate of batsman 1",strike1)
print("strike rate of batsman 2",strike2)
print("strike rate of batsman 3",strike3) 

print("Total runs if they played 60 more balls")
tot_runs1 = int(strike1*120/100)
tot_runs2 = int(strike2*120/100)
tot_runs3 = int(strike3*120/100)

print("Batsman 1:",tot_runs1)
print("Batsman 2:",tot_runs2)
print("Batsman 3:",tot_runs3)

max1= tot_runs1//6
max2= tot_runs2//6
max3= tot_runs3//6

print("\nMax 6 possible for 1st batsman:",max1)
print("Max 6 possible for 2nd batsman:",max2)
print("Max six possible for 3rd batsman:",max3)
