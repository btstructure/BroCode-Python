#dictionary - a changeable, unordered collection of unique key:value pairs, fast because they use hasing, allow us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}


#instead of using a numbered index, you must use the associated key to access the value

# print(capitals["Russia"])

#a safer way to access is to use a get method
print(capitals.get("Germany"))

#to add a new key value pair
capitals.update({"Germany":"Berlin"})

#to change the value of the key
#capitals.update({"USA": "Las Vegas"})

#will remove the key value pair
#capitals.pop("China")

#will clear the dictionary
#capitals.clear()

#will print all the keys
print(capitals.keys())

#will print only the values
print(capitals.values())

#to display all the key value pairs
print(capitals.items())

#will iterate once for the key and values in the dictionary
for key,value in capitals.items():
    print(key, value)

