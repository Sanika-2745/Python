# #Q1:
# def msg():
#     print("Hello sanika,How are you..!")
# msg()


# #Q2:
# def friend(name):       #\\ name=parameter;
#     print("my name is:",name)
# friend("sanika")        #\\ sanika=argument;

# # #Q3:
# def info(fname,lname,age,address):
#     print(fname,lname,age,address)
# info("sanika","chougale",20,"kolhapur")
# info("gauri","bhandigare",20,"gargoti")
# info("rucha","mhapsekar",20,"radhanagari")


#Q4:(using * arbitary/assetaric)
# def data (*kids):
#     print(kids)
# data("sanika","chougale",20,"radhanagari")

# #Q5:
# def foods (fruits):
#     for i in range(len(fruits)):
#         print(i,fruits[i])
# foods(["apple","mango","banana","graps","kiwi"])

#Q6:

# def cal(num1,num2):
#     add=num1+num2
#     sub=num1-num2
#     mul=num1*num2
#     div=num1/num2
#     print("addition of two numbers:",add)
#     print("substraction of two numbers:",sub)
#     print("multiplication of two numbers:",mul)
#     print("division  of two numbers:",div)
# cal(25,20)

# #Q7:
# def cal(num1,num2):
#     return num1+num2
#     print(cal(20,12))
# print(cal(25,12))

#Q5:write a program to check num is prime or not:

# def checkprime (num):
#     count=0
#     for i in range(1,num+1,1):
#         if num%i==0:
#             count+=1
#     if count==2:
#             print("num is prime") 
#     else:
#             print("num is not prime")       
# checkprime(4)            

#Q6:write a program prime numbers 1 to 100:
#case1:
# def primeno():
#     for i in range (1,101,1):
#         count=0
#         for j in range(1,i+1,1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i,end=" ")
# primeno()
#case2:
# def primeno():
#     count=0
#     for i in range (2,101,1):
        
#         for j in range(2,i+1,1):
#             if i%j==0:
#                 count+=2
#                 break    
#         if i==j:
#             print(i,end=" ")
# primeno()

