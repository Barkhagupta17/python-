#Write a function countMarks() which accepts marks and its size as an argument and to count the
#number of students who score than or equal to 60 marks and who score less than or equal to 33 marks.

marks=[]
def countMarks(num,size):
    marks60=marks33=0
    print "Marks Are="
    for i in range(len(num)):
        if marks[i]>=60:
            marks60=marks60+1
        else:
            marks33=marks33+1
    print "Total Students Who Score More Than or equal to 60 marks are=",marks60
    print "Total Students Who Score More Than or equal to 33 marks are=",marks33

size=input("Enter Total Number of Students=")
for i in range(size):
    smarks=input()
    marks.append(smarks)
countMarks(marks,size)
