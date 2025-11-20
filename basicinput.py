print("Welcome! Please input the following information.")
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

print("Welcome to the Math Quiz!")
score = 0
   
answer1 = input("What is 5 + 3? ")
if answer1 == "8":
    score += 1

answer2 = input("What is 10 - 4? ")
if answer2 == "6":
    score += 1

answer3 = input("What is 7 * 2? ")
if answer3 == "14":
    score += 1

answer4 = input("What is 20 / 5? ")
if answer4 == "4":
    score += 1

answer5 = input("What is 9 + 6? ")
if answer5 == "15":
    score += 1

answer6 = input("What is 12 - 3? ")
if answer6 == "9":
    score += 1

answer7 = input("What is 4 * 3? ")
if answer7 == "12":
    score += 1

answer8 = input("What is 16 / 4? ")
if answer8 == "4":
    score += 1

answer9 = input("What is 11 + 7? ")
if answer9 == "18":
    score += 1

answer10 = input("What is 15 - 5? ")
if answer10 == "10":
    score += 1

print(f"Quiz completed!")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Address: {address}")
print(f"Score: {score} out of 10")