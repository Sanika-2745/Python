#using string
# singer="rahul deshpande"
# print(singer)
# print(singer[0])
# print(singer[1])

# i=0
# while i<len(singer):
#     print(i,singer[i])
#     i+=1

#using list:

# friend=["sanika","gauri","rucha","vaishanvi","arpita"]
# print(friend)
# i=0
# while i<len(friend):
#     print(i,friend[i])
#     i+=1

#write a program sum of natural number
#case1:(step by sum)
# num=int(input("enter the num:"))
# sum=0
# for i in range (1,num+1,1):

#     sum=sum+i
#     print(sum)

#case2:(direct sum)
# num=int(input("enter the num:"))
# sum=0
# for i in range (1,num+1,1):

#     sum=sum+i
# print(sum)    

#write a program find factorial of numbers:
# num=int(input("enter the num:"))
# fact=1
# for i in range(1,num+1,1): 
#     fact=fact*i
# print(fact)

# #write a program find 1 to 100 even numbers:
# for i in range(1,101,1):
#     if i%2==0:
#         print(i,end=" ")


# #write a program find 1 to 100 odd numbers:
# for i in range(1,100,1):
#     if i%2!=0:
#         print(i,end=" ")

#write a  program to print divisible by 5 and 7 for 1to 1000:
# for i in range (1,1001,1):
#     if i%5==0 and i%7==0:
#         print(i,end=" ")

# for i in range (1,1001,1):
#     if i%5==0 or i%7==0:
#         print(i,end=" ")

#write a program to find multiplication of table:
for i in range(1,11,1):
    for j in range(1,11,1):
        print(i*j,end=" ")
    print()
