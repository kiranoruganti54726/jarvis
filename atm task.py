'''
step-1
take user name and password
step-2
ask user name and password
step-3
withdraw
credit
ministatement
'''
uname="kiran"
password1="kiran@12345"
username=input("enter your username:")
password=input("enter your password")
if username==uname and password==password1:
    print("1.money withdraw")
    print("2.credit")
    print("3.mini statement")
    a=int(input("please choose one option"))
    if a==1:
        cash=int(input("enter cash:"))
        print(cash,"is withdrawan")
    elif a==2:
        print("amount credited")
    elif a==3:
        print("this is your mini statement")
else:
    print("please enter valid credentials")