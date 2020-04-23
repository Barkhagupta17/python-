#Write program to accept n numbers containing positive and negative from the console and store them
#in two separate arrays called positivearray and negativearray. Calcualte and print the total of all
#positive and negative numbers and also print their sum
positivearray=[]
negativearray=[]
totalnumber=input("Enter Total Number of Elements=")
i=0
while(i<totalnumber):
    num=input()
    if num>0:
        positivearray.append(num)
    else:
        negativearray.append(num)
    i=i+1
print "The Positive Number List is=",positivearray
print "The Negative Number List is=",negativearray

sumpositive=0
sumnegative=0
for i in range(len(positivearray)):
    sumpositive=sumpositive+positivearray[i]

for i in range(len(negativearray)):
    sumnegative=sumnegative+negativearray[i]

print "Sum of Positive Numbers=",sumpositive
print "Sum of Negative Numbers=",sumnegative
