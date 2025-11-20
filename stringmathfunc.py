food = ["Menudo", "Kaldereta", "Adobo", "Sinigang", "Lechon"]
moreFood = input ("Put a food you want: ")
food.append(moreFood)
print (food)    

removeFood = input ("Put a food you want to remove: ")
food.remove(removeFood)
print (food)

cars = ("Toyota", "Honda", "Ford", "Chevrolet", "Nissan")
print (cars)
#using cars.remove("Ford") will give an error because tuples are immutable

Hobby1 = {"Watching", "Reading", "Skating", "Playing", "Listening to Music", "Walking"}
Hobby2 = {"Skating", "Touching Grass", "Playing", "Sleeping", "Drawing", "Reading"}
print (Hobby1.union(Hobby2))
print (Hobby1.intersection(Hobby2))
print (Hobby1.difference(Hobby2))