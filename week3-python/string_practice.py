#Part 2 -- Variables & Srings
#Task 1
first_name = "Ubeydah"
print(first_name)

last_name = "Yussuf"
print(last_name)

age = 19
print(age)

favourite_concept = "Git and Github"
print(favourite_concept)

#Task 2 : Concatenating
#Concatenating using the + operator
full_name = first_name + " " + last_name
print(full_name)

#Concatenating using the f string
full_name = print(f"{first_name} {last_name}")

#Task 3 : String methods
full_name = (f"{first_name} {last_name}")

#Uppercase
print(full_name.upper())

#Lowercase
print(full_name.lower())

#Count
print(full_name.lower().count("a")) 

#Index
print(full_name.find(" "))

#Replace
print(full_name.replace(first_name, "Coder"))

#Task 4 : F-string
print(f"Hi, I am {full_name}. I am {age} years old and my favourite concept so far is {favourite_concept}")

#Task 5 : Indexing and slicing
#First character
print(full_name[0])

#Last character
print(full_name[-1])

#Slice
print(full_name[0:7])
