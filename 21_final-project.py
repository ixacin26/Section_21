# 1. Ask for user input, a pokemon-character
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the URL in step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data
############################################################
import requests

character = input("Choose a character from the Pokemon-universe: ")

req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{character}")
charac = req.json()
abilities = charac["abilities"]
print(abilities[0]["ability"]["name"])


print(f"Data-type of charac: {type(charac)}")
# print(charac)


print(f"The name of the chosen character ist {charac["name"].capitalize()}")
print(f"The height of {charac["name"].capitalize()} is {charac["height"]}")
print(f"The weight of {charac["name"].capitalize()} is {charac["weight"]}")
print(f"{charac["name"].capitalize()} has the following abilities: {charac["abilities"]}")
# print(f"Data-type of Abilities: {type(abilities)}")
# print(abilities)
# print(abilities[1])

# try:
#     print(respone.json())
# except:
#     print(charac)

# for i in charac:
#     print(charac[i].keys())


# for i in charac:
    # print(charac[i].keys())
    # print(charac[i])

# print(charac["weight"])


