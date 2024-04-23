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

print(charac)


# try:
#     print(respone.json())
# except:
#     print(charac)

# for i in charac:
#     print(charac[i].keys())

# print(charac["abilities"])
# for i in charac:
    # print(charac[i].keys())
    # print(charac[i])

# print(charac["weight"])


