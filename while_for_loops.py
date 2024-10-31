####### while loops execute some code while a condition stays true ######


#while loops and for loops are forms of iteration
#iteration is the process of repeating or loopng through a set of instruction
#be careful of infinite loops as they will crash your program





# name = input("Enter your name")

# while name == "":
#     print("YOU DIDNT ENTER A NAME!")
#     # name = input("Enter your name")
# print(f"hello {name}")

# age = int(input("enter your age"))
# while age <0:
#     print("Age can't be negative!")
#     age = int(input("enter your age"))

# print(f"you are {age} years old")

# food = input("what do you like to eat? (Q to quit)")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("what do you like to eat? (Q to quit)")

# print("bye")

# num = int(input("enter a number between 1-10"))

# while num <1 or num >10:
#     print(f"{num} is not valid!")
#     num = int(input("enter a number between 1-10"))

# print(f"your number is {num}")



###### For loops execute a block of code a fixed number of times and you can iterate over a stringe, range, sequence, etc ######

# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)




# for x in reversed(range(1, 11, 3)):
#     print(x)
# # print("Happy new year!")




#X can also be named 'counter'

# for x in range(1, 21):
#     if x == 13 or x==15 or x==19:
#       break  # continue 
#     else: 
#         print(x)
#continue skips over the number/value specified
        


#challenge
horror_movies = ['The Excorcist', 'The Shining', 'The Conjuring', 'The Ring']
#if the anme is 'the shining' print it
#otherwise print 'the shining was not found!'
#out the other names using a loop
for movie in horror_movies:
    if movie == 'The Shining':
        print('The Shining was found!')
        print(movie)
        break
    else:
        print("The shining was found!")
        print(movie)

#challenge 2
#make a list of horror movie characters
#loop through the list and if "freddy krueger" is found, skip it and print the rest of the names
        
characters = ["Chucky", "Freddy Krueger", "Pennywise", "Jason"]
for character in characters:
    if character == "Freddy Krueger":
        continue
    print(character)

#challenge 3
#make a list of horror movie monsters, if a monster is named "swamp thing" then replace it with something else and print out the rest with the replaced name
monsters = ["Swamp thing","The thing", "Xenomorph", "predator"]
for monster in monsters:
    if monster == "Swamp thing":
        monsters.remove("Swamp thing")
        monsters.append("Dracula")
    print(monsters)