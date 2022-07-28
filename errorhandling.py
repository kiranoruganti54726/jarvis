'''
try=risky code or errors vache code rastham illa
except=try lo error osthe code terminate kakunda suskuntadhi
else=try lo error rakapothe else execute aithadi
finally=try lo error vachina rakapoina execute aithadi
'''
try:
    print(kiran)
except:
    print("i am except,try lo error osthe nen execute aitha")
else:
    print("i am else,try lo error rakapothe nen execute aitha")
finally:
    print("i am ly finally,try lo error achina rakapoina execute aitha")

a="string"
try:
    print(int(a))#we cannot convert string to integer
except Exception as k:#manaki error telvakapothe write this code
    print(k)
    print("paina error print chesindi nenu except block")


#multiple errors unte multiple try and except undali

lst=[0,1,2,3]
try:
    a=1/0
    print(a)
except Exception as ab:
    print("this is error",ab)

try:
    print(lst[4])#4th index value lene ledhu
except Exception as abc:
    print(abc)