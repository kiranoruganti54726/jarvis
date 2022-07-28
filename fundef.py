# #from userdefined_module import degree
# #we can  call only degree function using above import statement
#
# from userdefined_module import *
# degree()
# btech()
# pharmacy()
# pg()

from datetime import datetime

now = datetime.now().time() # time object

print("now =", now)
print("type(now) =", type(now))