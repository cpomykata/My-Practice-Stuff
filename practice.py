
#birthyear = input("What is your birth year ")
#birthmonth = input("What is your birth month (in numerical) ")

#age = 2022 - int(birthyear)
#age2 = 0 + int(birthmonth)

#print(age, "years and ", age2, "months old")

#first = input("First ")
#second = input("Second ")
#sum = float(first) + float(second)
#print("Sum is", sum)

#course = "pythoniscool"

#print(course.upper())
#print(course.find("o"))
#print(course.capitalize())
#print(course.replace("cool", "rad"))
#print(course.find("python"))#this shows the index/starting number of where it is
#print("python" in course)
#arithmatic
#print(10+3)  #+-/*
#print(10/3)
#print(10//3)
#print(10**3)

# operators
#x = 10
#x = x+3
#x += 3
#print(x)

#x = (10 + 3) * 2

#x = 3 > 2 #< >= <= == != either true or false
#print(x)

#price = 5
#print(price > 10 and price <30)
#print(price > 10 or price <30)
#print(not price > 10) # turns true to false or vice versa

#temp = 5
#if temp > 35:
    #print("Its a hot day out")
#elif temp  > 20:
    #print("Its not bad out")  
#elif temp > 10:
    #print("Its a bit cold")
#else:   
    #print("its cold")
#my solution
#weight = input("What is your cureent weight? ")
#kg_lbs = input("Is that (K)g or (L)bs? ")
#if kg_lbs == "K":
    #print(float(weight) * 2.2)
#elif kg_lbs == "L":
    #print(float(weight) / 2.2)

#his solution
#weight = int(input("Weight: "))
#unit = input("(K) or (L)bs: ")
#if unit.upper() == "K":
    #converted = weight / 0.45
    #print("Weight in Lbs: ",  converted)
#else:                                       #string or comma seems to work the same
    #converted = weight * 0.45
    #print("Weight in Kgs: ",  str(converted))

#print(1)
#print(2)
#print(3)
#Print(4)
#very ineficent 
#instead we can do this

#i = 1
#while i <= 1_000:   #apparently it reads it as 1,000
    #print(i)
    #i = i + 1
#i = 1
#while i <= 10:   #apparently it reads it as 1,000
    #print(i * '*')
    #i = i + 1

#lists

#names = ["John", "Bob", "Mosh,", "Same", "Corbin"]
#names[0] = "Jon"
#print(names[0])
#print(names)
#print(names[0:3])

#list methods

#numbers = [1, 2, 3, 4, 5]
#numbers.append(6) #inserts this at the end of the list
#numbers.insert(0, -3) #inserts at the beginning of the list
#numbers.remove(3) #remove 3 from list
#numbers.clear() #clear list
#print(10 in numbers) #true or false
#print(len(numbers)) #how many elements are in a list
#print(numbers)

#for loops
numbers = [1 ,2, 3, 4, 5]
for item in numbers:
    print(item * "x")

#i = 0
#while i < len(numbers):    #top one is easier than this one
    #print(numbers[i])
    #i = i + 1

#range fucntions
#numbers = range(5)
#numbers = range(5, 10)  #starts at 5 and ends at 9
#numbers = range(5, 10, 2) # the 2 is a step meaning it jumps by 2
#print(numbers) #prints (0,5)
#for number in numbers:
    #print(number)
#for number in range(5):
    #print(number)

#tuples
#numbers = (1,2,3,3) 
#numbers.count(3)
#print(numbers)

