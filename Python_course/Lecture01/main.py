
bill=print(int((input("what is your total shoping bill? : "))))

if bill >= 25000:
    print("congratulation you got 25 discount on your shoping.!")

elif bill >= 20000 and bill < 25000:
    print("congratulation you got 20 discount on your shoping.! ")

elif bill >= 15000 and bill < 20000:
    print("congratulation you got 15 discount on your shoping.! ")

elif bill >= 10000 and bill < 15000:
    print ("congratulation you got 10 discount on your shoping.! ")
else:
    print("Sorry you are not eligible for discount offer.! ")