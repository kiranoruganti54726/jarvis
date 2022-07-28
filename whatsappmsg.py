import pywhatkit
import pywhatkit as pwk
#sending msg to individual contact
contacts={"mom":"+919652261371","teja" : "+918499086087","shalini":"+919100891759"}
names_list=list(contacts.keys())#converts keys to list

flag1=True
while flag1:
    name=input("enter Contact Name to send a msg:")
    if name=="exit":
        break
    elif name in names_list:
        number=contacts[name]
        print(number)
        #hour = int(input("enter time hour in 24 hour format :1 to 24 here:"))
        #minutes = int(input("enter minutes(0-60) here"))
        msg=input("what msg u want to send:")
        pywhatkit.sendwhatmsg_instantly(number, msg)#pywhatkitsends msg instantly
        #pywhatkit.sendwhatmsg_instantly(number,msg, 15, True, close_time=3)
        print(contacts[name])
    else:
        print("plz enter a number from available contact list")

# hour=int(input("enter time hour in 24 hour format :1 to 24 here:"))
# minutes=int(input("enter minutes(0-60) here"))
# pywhatkit.sendwhatmsg(contacts[name],"hi",hour,minutes,15,True,close_time=3)














# phonenumber="+91"+input("enter phone number:")
# msg=input("enter the msg u want to send:")
# hour=int(input("enter time hour in 24 hour format :1 to 24 here:"))
# minutes=int(input("enter minutes(0-60) here"))
#pywhatkit.sendwhatmsg(phonenumber,msg,hour,minutes,15,True,close_time=3)
#15=waittime for msg delivery,True=closes the tab after msg delivery,close_time=in 3 seconds tab will be closed
