import random


firstname = input("What is your first name? ")
lastname = input("What is your last name? ")

print("Hi there, " + firstname + " " + lastname + ", " + "nice to meet you!")

age = int(input("How old are you? "))


if (age < 100):
   print(str(age) + " You're old")
elif (age > 100):
   print(str(age) + " You're old")
else:
   print("Is a good age")  

fav = int(input("Whats your favorite number? "))


if (fav <= 50):
    print(str(fav) + " That's interesting")
elif (fav == 4):
    print(str(fav) + " Same!")
else:
   print("That's cool")  
   
feeling = input("How are you feeling today?")
   
x = random.choice(["That's good to hear", "Interesting", "I see."])
print(x)
