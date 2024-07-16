# 2D lists = a list of lists // multi dimensional lists

drinks = ["coffee", "sode", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0][0])   # prints coffee
print(food[2][1])   # [first list][second list]


dice = ["dice cata", 'yahtzee', 'dice party']
strategy = ['chess', 'checkers', 'catan']
fun = ['Muffin time', 'Uno', 'pickup stix']


games = [dice, strategy, fun]

print(games[0][2])