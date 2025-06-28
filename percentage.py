per=int(input("enter the percentage"))
if per>=75 and per<=100:
    print("destination")
elif per>=60 and per<=74:
    print("first class")
elif per>=50 and per<=59:
    print("second class")
elif per>=35 and per<=49:
    print("pass class")
elif per<35:
    print("fail")

else:
    print("persentage is invalid")
