# dictionary = A changeable, unordered, collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly
# think Key: Value

# order the array from order the numbers from 1-9
# example input = [6, 5, 3, 1, 2, 4]
# output: [1, 2, 3, 4, 5, 6]

# must use a dictionary
# you can use the sort method

s = [6, 5, 3, 1, 2, 4]

news = {}

for nums in s:
    news[nums[0]] = num

print(news)













#s = [6, 5, 3, 1, 2, 4]

#for num in s:
    #s.sort()

#print(s)













capitals = {'USA':'Washington D.C.',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China') # Removes key value pair
#capitals.clear()

#print(capitals['Russia'])       this one is risky
#print(capitals.get('Germany'))  this one is safe
#print(capitals.keys())
#print(capitals.values())

#print(capitals.items())

for key, value in capitals.items():
    print(key, value)