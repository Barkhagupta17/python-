num=[30,20,30,40,30] # Create a list and assigned some values
for i in range(5):
    print num[i]
total=avg=0

for i in range(5):
    total=total+num[i]
    avg=total/5
print "Total =",total
print "Average=",avg
