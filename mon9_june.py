# #write a program display reverse numbers:
# def rev_num(num):
#     rev=0
#     while num>0:
#         rem=int(num%10)
#         rev=(rev*10)+rem
#         num=int(num/10)
#     print("Reverse numberis:",rev)
# rev_num(123)

#write a program to check num is palindrom or not:
# def palindrom(num):
#     temp=num
#     pal=0
#     while num>0:
#         rem=int(num%10)
#         pal=(pal*10)+rem
#         num=num//10
#     if temp==pal:
#         print("palindrome")
#     else:
#         print("not palendrome")
# palindrom(121)

#write a program to check nos is armstreong ore not:
# def checharmstrong(num):
#     arm=0
#     temp=num
#     while num>10:
#         rem=num%10
#         arm=(rem*rem*rem)+arm
#         num=num//10
#     if temp==arm:
#         print("num is armstrong")
#     else:
#         print("num is not armstrong")
# checharmstrong(153)

#write a program to find febonacci:
# def febo(num):
#     a=0
#     b=1
#     print("a=",a)
#     print("b=",b)
#     for i in range(1,num+1,1):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
#febo(6)

#write a program for swipping two numbers and print it:
# def swap (a,b):
#     temp=a
#     a=b
#     b=temp
#     print("a=",a)
#     print("b=",b)
# swap(25,30)

# #writea program to find factorial:
def fact(num):
    fact=1
    for i in range(1,num+1,):
        fact=fact*i
        print("factorial num is:",fact)
fact(5)