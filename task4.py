num=20                   #num is a variable that is storing 20 which is an integer datatype
dec=20.5                 #float datatype
name="kiran oruganti"    #string datatype
com=3+5j                 #complex number
b1=True
b2=False
a=2
b=4
print('-------------values before type conversion---------------')
print(" integer number=",num,"\nfloat number =",dec,
      "\nstring=",name,"\ncomplex number=",com,"\nboolean values=",b1,",",b2,"\na=",a,"\nb=",b)


print('-------------values after type conversion---------------')
num1=float(num)#implicit type conversion
dec1=int(dec)#explicit type conversion
c=complex(a,b)
print(" integer number=",num1,"\nfloat number =",dec1,
      "\nstring=",name,"\ncomplex number=",com,"\nboolean values=",b1,",",b2,"\na=",a,"\nb=",b,
      "\ntype converted a and b to complex number=",c)



