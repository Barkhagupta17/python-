num=[] #an empty list
print "Enter any 10 numbers="
for i in range(10):
    number=input()
    num.append(number)
ev=0
od=0
for i in range(10):
    if num[i]%2==0:
        ev=ev+1
    else:
        od=od+1
print "Total Even Numbers are=",ev
print "Total Odd Numbers are=",od
