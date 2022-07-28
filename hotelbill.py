uname=input("enter the username:")
password=input("enter your password")
sum=0
i=True
if uname =="kiran" and password=="kiran@1234":
    print("-"*60)
    print(" "*20,"welcome to kiran hotels"," "*20)
    rooms={"single":10000,"double":20000,}
    rooms_lst=list(rooms.keys())
    #print(rooms_lst)
    food={"single biryani":140,"plate biryani":260,"family pack biryani":440}
    food_lst=list(food.keys())
    #print(food_lst)
    wifi_perhour=100
    pool={"singles":1000,"couples":2000,"family":4500}
    pool_lst=list(pool.keys())
    #print(pool_lst)
    while i:
        #room category

        print("-" * 60)
        print(' '*20,"available rooms ",' '*20)
        print("single=10000 ")
        print("double=20000")
        r1=input("please select a room:")
        if r1 in rooms_lst:
            sum=sum+rooms[r1]
            room_originalcost=sum
            print(room_originalcost)
            room_gst=(room_originalcost*5)/100
            print("gst of room=",room_gst)
            room_fullpay=room_originalcost + room_gst
            print(room_fullpay)
        else:
            print("please choose from available")
            continue

#food category

        print("-" * 60)
        print(' '*20,"available foods",' '*20)
        print("single biryani")
        print("plate biryani")
        print("family pack biryani")
        f1=input("please select a food:")
        if f1 in food_lst:
            sum=sum+food[f1]
            food_originalcost=food[f1]
            print("food original cost=",food_originalcost)
            food_gst=(food_originalcost*5)/100
            print(food_gst)
            food_fullpay=food_gst+food_originalcost
            print(sum)
        else:
            print("please choose from available")

#wifi category

        print("-" * 60)
        print(' '*20,"wifi service per hour=",wifi_perhour,' '*20)
        wifi1=input("press yes for wifi service and no if you dont want it :")
        if wifi1=="yes" or wifi1=="Yes" or wifi1=="YES":
            w=int(input("how many hours do you want :"))
            sum=sum+ wifi_perhour*w
            wifi_originalcost= wifi_perhour * w
            wifi_gst= (wifi_originalcost * 5) / 100
            wifi_fullpay= wifi_gst + wifi_originalcost
            print(sum)

        elif wifi1=="no"or wifi1=="NO"or wifi1== "No":
            print("thats fine")

#pool category

        print("-" * 60)
        print(' '*20,"pool services ",' '*20)
        print("for singles=",pool["singles"])
        print("for couples=",pool["couples"])
        print("for family=",pool["family"])
        p=input("please choose a category if not interested in pool enter 'no':")
        if p== "yes":
            p1=input("select a pool category:")
            if p1 in pool_lst:
                sum=sum+pool[p1]
                pool_originalcost=pool[p1]
                pool_gst=(pool_originalcost*5)/100
                pool_fullpay=pool_originalcost+pool_gst
                print(sum)
        elif p== "no" or p== "NO" or p== "No":
            print(sum)

#bill generation code
        print("-" * 60)
        a=input("press 'p' to proceed for the bill:")
        if a=="p" or a=="P":
            name=input("please enter your name:")
            address=input("enter your address:")
            uid=int(input("enter your aadhar number:"))
            print("-"*100)
            print(" "*40,"kiran hotels and services"," "*40)
            print(" "*45,"INVOICE BILL"," "*45)
            print("-" * 100)
            print("customer name=",name)
            print("address=",address)
            print("aadhar=",uid)
            print("-"*100)
            print("sno", " " * 5, "services", " " * 15,
                  "price", " " * 15, "gst", " " * 20, "net amount")
            print("-"*100)
            services = ["rooms", 'food', 'wifi', 'pool']
            r11="rooms"
            f22="food"
            w22="wifi"
            p22="pool"
            for r11 in services:
                print(1," "*5,"room","(",r1,")"," "*10,rooms[r1]," "*15,room_gst," "*20,room_fullpay)
                break
            for f22 in services:
                print(2," "*5,"food","(",f1,")"," "*4,food[f1]," "*17,food_gst," "*22,food_fullpay)
                break
            for w22 in services:
                if wifi1=="yes":
                    print(3," " * 5, "wifi","(",wifi_perhour,"perhour",")", " " * 7, wifi_originalcost," "*17,wifi_gst," "*21,wifi_fullpay)
                    break
                else:
                    print(3," " * 5,"wifi","(",wifi1,")", " " * 10)
                    break
            for p22 in services:
                if p== "yes":
                     print(4," " * 5,"pool","(",p1,")"," " * 10, pool[p1], " " * 17, pool_gst, " " * 20, pool_fullpay)
                     break
                else:
                    print(4," " * 5, "pool", " " * 10,)
                    break
            print("-"*100)
            gst=(sum*5)/100
            print(" "*75,"gst =",gst)
            print(" "*66,"total amount =",sum)
            print(" "*62,"payable amount =",gst+sum)
            print("-" * 100)
            i=False
else:
    print("-"*20,"please enter valid user name and password","-"*20)
