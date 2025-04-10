# problem 1
#age = input("what's your age")
#name = input("what's your name")

#print(name, age, type(name), type(age))

#problem 2
# Ask the user for the two numbers
#first_number = input("what's the first number")
#second_number = input("what's the second number")

# convert the numbers to integer versions of themselves
#fist_number = int(firsit_number)
#second_number = int(second_number)

#compare the two numbers
#if first_number > second_number:
#    print(first_number, "is bigger")
#elif first_number == second_number:
#    print("the numbers are equal!")
#else:
#    print(second_number, "is bigger")

#problem 5
while " " in name:
    name = name.replace(" ", "")
#Ask the user for their name and save in varaible called name
name = input("what's your full name")
#Calculate the length of name
length_of_name = len (name)
#print the length
print(length_of_name)