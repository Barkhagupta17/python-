#Write a function countThe() to count the word 'the' or 'The' as an independent word in a text file "Story.txt"
#for example, if the content of the file "Story.txt" is
#Monkeys are one of the funiest animals in the nature.
#Monkeys live in the forests.
#There was a monkey in the zoo. The monkey was very naughty.
import os
def countThe():
    if os.path.isfile("Story.txt"):
        fobj=open("Story.txt","r")
        count=0
        while True:
            str=fobj.readline()
            if not str:
                break
            str=str.split()
            for i in range(len(str)):
                if str[i]=='the' or str[i]=='The':
                    count=count+1
        print "Total Count is=",count
    else:
            print "File does not exist"
    
countThe()
