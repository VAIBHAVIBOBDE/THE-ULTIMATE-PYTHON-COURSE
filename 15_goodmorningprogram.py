import time
#error
timestamp=time.strftime('%h:%m:%S')
print(timestamp)
timestamp=time.strftime('%h')
print(timestamp)
timestamp=time.strftime('%m')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)
#timestamp=hr,m,sec,   strftime=converting time
import time
timestamp=time.strftime('%m:%h:%S')
print("timestamp")
#error
import time
h = int(time.strftime('%H'))
m = int(time.strftime('%M'))
s = int(time.strftime('%S'))
print(h)
print(m)
if(h==0 or h<=11):
    if(m>0 and m<=59):
        if(s>0 and s<=59):
            print("Good Morning")
elif(h>=12 and h<=16):
    if(m>0 and m<=59):
        if(s>0 and s<=59):
            print("Good Afternoon")
elif(h>=17 and h<=21):
    if(m>0 and m<=59):
        if(s>0 and s<=59):
             print("Good Evening")
else:
    print("Good Night")
#perfect code
import time
x= input("enter the time (24:00): ")
y= x[0:2]
z= int(y)

if (z<12>4):
    print("Good Morning !")
elif (z==12):
    print("Good Noon !")
elif (z<17>12):
    print("Good Afternoon !")
else:
    print("Good Evening !")