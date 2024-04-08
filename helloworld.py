# def check_traffic_signal(color):
#     if color.lower() == "red":
#         print("Stop")
#     elif color.lower() == "yellow":
#         print("Prepare to stop")
#     elif color.lower() == "green":
#         print("Go")
#     else:
#         print("Invalid color")

# # Example usage:
# traffic_color = input("Enter the color of the traffic signal: ")
# check_traffic_signal(traffic_color)

# fruits = ["orange","grapes","banana"]
# x,y,z = fruits

# print(x,y,z)

    
# x = "global variable"
# y = "global y value called outside of function"

# def myFunction():
#     x = "is local funtion value for x"
#     print("this is" +" "+ x)

#     global y
#     y = "variable declared global"

# myFunction()

# print("This is gloabl value of" +" "+x)
# print(y)

# x =1j

# print(type(x))

# import random

# print(random.randrange(1,10))


# #slicing

# a = "hello, world!"

# print(len(a))
# print(a[2:])
# print(a[-5:-2])

#using Format to insert numbers into a string

# quantity = 3
# itemno = 56
# itemPrice = 103.22

# myOrder = "I want {} pieces of item {} for {} dollars"
# print(myOrder.format(quantity,itemno,itemPrice))


# stringMethods = "happy birthday"
# print(stringMethods.capitalize())
# print(stringMethods.casefold())
# print(stringMethods.center(20))
# print(stringMethods.encode())
# print(stringMethods.find("a"))

#practicing list


# print("************")

# newList = myList[3:]
# print(newList)
# print("************")

# newList[1:2] = ["orange","watermelon"]
# print(newList)
# print("************")
# newList.append("dragon fruit")
# print(newList)
# print("************")

# myList.insert(1,"guava")
# print(myList)
# print("************")

# myList.extend(newList)
# print(myList)
# print("************")

# myList.remove("guava")
# print(myList)
# print("************")

# print("length of the list is",len(myList))

# for i in range(len(myList)):
#     print(myList[i])

# myList.pop(0)
# print(myList)

myList = ["apple","banana","mango","grapes","kiwi","melon"]

for i in myList:
    if "a" in i:
        print(i)

newlist = [x for x in myList if "a" in x]
print(newlist)

newlist = [x.upper() for x in myList if x !="apple"]
print(newlist)

newlist = [x for x in range(10) if x<5]
print(newlist)

newlist = [x if x !="banana" else "orange" for x in myList]
print(newlist)