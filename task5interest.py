#SI Formula	S.I. = Principal × Rate/100 × Time
#CI Formula	C.I. = Principal (1 + Rate)Time/100 − Principal
'''amount=float(input("enter the amount"))
rate=float(input("enter the interest rate"))
time=float(input("enter the time"))
ch=int(input("choose 1 for simple interest(SI) \nchoose 2 for compound interest (CI)\n"
             ":"))
if ch==1:
    print("payable amount =",(amount * rate * time)/100)
elif ch==2:
    print("payable amount =",amount *(1+rate/100)**time -amount)'''
'''services=["rooms","wifi",54,22]
print("sno"," "*5,"services"," "*5,"price"," "*5,"gst"," "*5,"net amount"," "*5)
services=["rooms","wifi",54]
sno=len(services)
room=2000
room_gst=250
wifi=200
pool=2000
food=140
i=0
print("")'''
from jarvis_with_sound import *

print('-'*59)
print(" "*50,room_gst," ")