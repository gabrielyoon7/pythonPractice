def calc():
    global fee
    global sauna
    if age>=65:
        fee=fee-1000
    elif age<=7:
        fee=fee-2000
    
    if hour<=5 or hour>=20:
        fee=fee+2000
    if sauna=="y":
        sauna=1000
    else:
        sauna=0
    return
        
def bill():
    print("============================")
    print("Age : ", age)
    print("Entrance Time : ", hour)
    print("Sauna Fee : ",fee)
    print("Extra Sauna Clothes Fee: ", sauna)
    print("============================")
    print("Total Fee : ",fee+sauna)

    
import random
hour=random.randint(0,24)
fee=8000
age=int(input("AGE ? "))
sauna=input("Extra Sauna? y/n?")
calc()
bill()
