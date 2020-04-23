#Write a Function which accepts an integer array and its size as arguments and replaces elements
#having odd values with thrice their value and elements having even values with twice their value.
#For Example
#if an array num contains 7 elements as
#3 4 5 16 9 11 8
#then the output will be
#9 8 15 32 27 33 16
num=[]
def EvenOdd(a,s):
    for i in range(len(a)):
        if(a[i]%2==0):
            a[i]=a[i]*2
        else:
            a[i]=a[i]*3
    print "The Replaced Array is="
    for i in range(len(a)):
        print a[i]

size=input("Enter the Size of array=")
for i in range(size):
    number=input()
    num.append(number)
EvenOdd(num,size)
     
