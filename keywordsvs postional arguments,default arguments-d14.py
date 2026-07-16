#key words and positionnal arguments


#arguments --------
#first argement is keyword and positional arguments
'''def Details(id,name,mailid):
    id =10
    name="sai"
    mailid="saikishnagudla556@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",maild="mailid")'''



'''
def Details(id,name,maildid):
    print(id,name,mailid)
Details(id ="id",name="name",mailid="mailid")

Details(id =20,name="manoj",mailid="m@gmail.com")

Details(id =30,name="harsha",mailid="h@gmail.com")


Detail(40,"trinadh","t@gmail.com")

Details("s@gmail.com",50,"sai")

Details(mailid="s@gmail.com",name="sumanth",id =30,)'''



#default  arguments

'''def Grocery(item,price):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery("sugar",200)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery("dhal")'''

'''def Grocery(item="ghee",price):
    #it will be error beacause first one should be always empty.
    print("item is %s"%item)
    print("price is %d"%price)
Grocery(500)'''




#task- cake_name,price,qty


def cake(name,price,qty):
    print("cake is %s" %name)

    print("price is %0.1f" %price)

    print("qty is %0.2f kg" %qty)


cake("red velvet",5000,1)






































