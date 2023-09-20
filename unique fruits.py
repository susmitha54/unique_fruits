fruit_basket = []
unique_fruits = []
for i in range(2):
    fruit = input("Enter a fruit:")
    fruit_basket.append(fruit)
for fruit in fruit_basket:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)
    print(unique_fruits)