# string example:
#Ex1:
# inst = "igap technology kolhapur"
# print(inst)
# print(inst[0])

#using for loop :
# inst = "igap technology kolhapur"
# for i in range(len(inst)):
#     print(i,inst[i])

#using while loop:
# inst = "igap technology kolhapur"
# i = 0
# while i<len(inst):
#     print(i,inst[i])
#     i+=1
# print(len(inst))

#slicing string:
# inst = "igap technology kolhapur"
# print(inst[2:10])
# print(inst[2:])
# print(inst[:10])
# print(inst[:])
# print(inst[2])

# concating string:
# inst = "igap technology kolhapur"
# dep = "computer science"
# print(dep)
# print(inst + " " +  dep)

### string methods:
# inst = "igap technology kolhapur"
# print(inst.upper())
# print(inst.lower())

# singer ="Rahul"
# print(singer)
#strip method:
# singer1 = "   Rahul   "
# print(singer1.strip())
#replace method:
singer ="Rahul is sTudent rahul"
# print(singer.replace("rahul","mahesh"))
# #split method
# print(singer.split("/"))
# #capitalize:
# print(singer.capitalize())
# #casefold method:
# print(singer.casefold())
#center method:
# singer ="Rahul Patil is student Rahul"
# print(singer.center(250))

singer ="Rahul Patil is student Rahul"
print(singer.count("Rahul"))

print(singer.find("Patil"))

print(singer.index("Rahul"))

print(singer.title())
print(singer.swapcase())

no = "5"
print(no)
print(no.zfill(2))

print(singer.endswith("ragini"))
print(singer.isalnum())











