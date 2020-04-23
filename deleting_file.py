#Demonstration of remove() method
import os
myfile="info1.txt"
if os.path.isfile(myfile):
    os.remove(myfile)
    print "File Successfully Deleted"
else:
    print "File does not exist"
