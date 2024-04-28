# 1. Ask for user input, a pokemon-character
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the URL in step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data
############################################################
import requests

character = input("Choose a character from the Pokemon-universe: ").lower()
req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{character}")

if req.status_code == 200:
    charac = req.json()
    abilities = charac["abilities"]
        
    print(f"\nThe name of the chosen character ist {charac["name"].capitalize()}")
    print(f"The height of {charac["name"].capitalize()} is {charac["height"]}")
    print(f"The weight of {charac["name"].capitalize()} is {charac["weight"]}")
    print(f"{charac["name"].capitalize()} has the following abilities:")

    # Using nested loops - got help from ChatGPT ;-)
    for ability in abilities:
        for key, value in ability.items():
            if isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    print(f"   {nested_key}: {nested_value}")
            else:
                print(f"   {key}: {value}")
        print()
else:
    print("No such character in Pokemon-Universe!")



