# print("hello world")

# if 5 > 2:
#     print("wow")

# x = "you"
# y = "are"
# z = "twenty"
# print(x,y,z)

# print (len(x))
# print (z[0:3])

# print(bool(x))


# ................python lists.................


# list = list(("joy" ,"love","peace","energy","wife","mine"))
# print(list)
# fruits = ["mango", "pineapple", "papaya"]
# print(fruits)
# print(list)
# print (len(list))
# print (list[2:4])
# list.insert(2,"watermelon")
# print (list)
# list.append("enemy")
# print (list)
# list.extend(fruits)
# print (list)
# list.pop(1)
# print (list)

# for x in range(1,4):
#     print(list[x])


# i = 0
# while i <5:
#     print(list[i])
#     i=i+1

# newlist=[]
# for x in list:
#  if "a" in x:
#     newlist.append(x)

#     print(newlist)

# newlist = [x for x in fruits if "a" in x]

# print(newlist)
# print(list.count("peace"))


# ................python tuples.................

# myTuple = ("kate","joy")
# print(myTuple)

# x = list(myTuple)
# print(type(x))
# x[0] ="kiwi"
# print(x)
# x.insert(1,"joan")
# print(x)
# x.append("victor")
# print(x)
# myTuple= x
# print(myTuple)

# print(myTuple.count("joy"))

# ................python sets.................

# thisset = {"joyce","ruger"}
# tropical ={"watermelon","mango","apple"}

# print(thisset)
# set3 =thisset.union(tropical)
# print(set3)

# ................python Dictionaries.................

# thisDict ={
#     "name":"kate",
#     "age":"20",
#     "location":"nairobi"

# }
# print (len(thisDict))
# print(thisDict.items())
# if "name" in thisDict:
#     print("yes I see it")

# thisDict["job"]= "engineer"
# thisDict.update ({"color":"pink"})
# print(thisDict)

#..........................python functions................

# def myFunction(fname):
#     print( fname + " "+ "ratemo")

# myFunction("kevin")
# myFunction("imma")
# myFunction("trina")

# 

#..................classes and objects......................
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class person :
    def __init__(self,age,name):
        self.age =age
        self.name =name 

p1 = person(15 , "john")
p2 = person(17 ,"mary")
print(p1.name,"is turning",p1.age,"tommorrow")

print(p2.name,"is turning",p2.age,"tommorrow")