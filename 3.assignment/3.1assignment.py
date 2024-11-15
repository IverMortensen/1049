# --- Exercise 1 ---
def str_crunch(text: str) -> str:
    """
    Removes white space and newlines from a string.
    """
    whiteSpace = {' ', '\n'} # Characters to exclude
    result = ""

    # Loop through each character in the text
    for char in text:
        # Add all characters that is not whitespace
        if char not in whiteSpace:
            result += char

    return result

def my_split(text: str, sep: str) -> list:
    """
    Splits a string into individual words.
    Words are split based on the separator.
    Separator needs to be a single character.

    Returns a list of the words.
    """
    word = ""   # Holds the current word
    result = []

    # Make sure the separator is a single character
    if len(sep) != 1:
        print("Separator needs to be a single character.")
        return []

    # Loop through each character in the text
    for char in text:
        # Add each character that is not the separator to the word
        if char != sep:
            word += char
        # If it is the separator, add the current accumulated
        # word to the result and start on the next word
        else:
            result.append(word)
            word = ""

    # If there is a remaining word, add it as well
    if word:
        result.append(word)
        
    return result

def str_occur(text, symbol) -> list:
    """
    Finds the indecies that a symbol occurs at in a text.

    Returns the indecies as a list of ints.
    """
    result = []

    # Make sure the symbol is a single character
    if len(symbol) != 1:
        print("Symbol needs to be a single character.")
        return []

    # Loop through each character in the text
    for index, char in enumerate(text):
        # If the symbol is found, add its index to the result
        if char == symbol:
            result.append(index)

    return result

# --- Exercise 2 ---
def get_colours(country_dict: dict, country: str) -> list:
    """
    Finds the colours in a country's flag.
    Takes a dict of country to flag map and the key of a flag.

    Returns the colours in a list.
    """
    # Find the colors of the country's flag
    try:
        colours = country_dict[country]

    # Catch if the country can't be found

    # Taks 2B explanation:
    # If the country can't be found in the dictionary we get a KeyError exception
    # as the countries are keys in the dictionary and the key can't be found.
    # This can be catched by checking for a KeyError exception.
    # If an exception isn't catched the program stops.
    except KeyError:
        # Re-raise the exeption with a message indicating what whent wrong
        raise KeyError(f"Can't find the country '{country}'")  
    
    return colours

def get_countries(country_dict: dict, colour: str) -> list:
    """
    Finds all countries that has a flag
    that contains the spesified colour.

    If no countries are found a ValueError is raised.

    Returns the countries in a list.
    """
    result = []

    # Loop through each country and flag colour pair in the dict.
    for country, flagColours in country_dict.items():

        # Loop through each colour in the flag colours.
        for flagColour in flagColours:
            # If the spesified colour is found,
            # the country is added to the result
            if flagColour == colour:
                result.append(country)

    # If no country is found a ValueError is raised
    if len(result) == 0:
        raise ValueError(f"No countries with the flag colour {colour}")

    return result

# --- Exercise 3 ---
def find_cheapest_shop(shops: dict, shopping_list: list) -> str:
    """
    Finds the cheapest shop out of the given shops
    to buy the items in the given shopping list.

    If not shop can be found a ValueError is raised.

    Returns the name of the cheapest shop.
    """
    cheapestShop = ""
    cheapestPrice = 1000000

    # Loop through each shop
    for shop in shops:
        totalPrice = 0      # Total price of the items in current shop
        hasAllWares = True  # Indicates if the current shop has all items

        # Get the wares the current shop has
        wares = shops[shop]

        # Loop through each ware in the shopping list
        for item in shopping_list:
            # Get the price of the current ware in the current shop
            try:
                warePrice = wares[item]
            
            # If an item can't be found in the shop update the
            # hasAllWares status and break out of the loop
            except KeyError:
                hasAllWares = False
                break
            
            # Add the ware price to the total
            totalPrice += warePrice
        
        # Skip shops that doesn't have all
        # the items in the shopping list
        if not hasAllWares:
            continue

        # Update the cheapest shop when
        # a new lower total price is found
        if totalPrice < cheapestPrice:
            cheapestPrice = totalPrice
            cheapestShop = shop
    
    # If no shop is found raise a ValueError
    if not cheapestShop:
        raise ValueError(f"Could not find a store containing all the items in the shopping list {shopping_list}")
    
    return cheapestShop

if __name__ == "__main__":
    # Exercise 1
    print("--- Exercise 1 ---")
    text = "This is a test message \nTest Testing Tested"
    print(f"Input text: \n{text}\n")

    # Task 1A
    result = str_crunch(text)
    print(f"Text without white space and newlines: \n{result}\n")

    # Task 1B
    sep = " "
    result = my_split(text, sep)
    print(f"Message separeated on \"{sep}\": \n{result}\n")

    # Task 1C
    symbol = "e"
    result = str_occur(text, symbol)
    print(f"Indecies of symbol \"{symbol}\": \n{result}\n")

    # Exercise 2
    print("--- Exercise 2 ---")
    flag_colours = {
    "norway" : ["red", "white", "blue"],
    "denmark" : ["red", "white"],
    "sweden" : ["blue", "yellow"],
    "finland" : ["white", "blue"],
    "japan" : ["red", "white"],
    "great_britain" : ["red", "blue", "white"],
    "chile" : ["blue", "white", "red"],
    "south_africa" : ["black", "yellow", "green", "white", "red", "blue"]
    }

    # Task 2A
    # Testing countries that exsist in the dictionary
    country = "norway"
    try:
        colours = get_colours(flag_colours, country)
        print(f"The flag of {country} has the colors {colours}\n")
    except KeyError as e:
        print(f"A KeyError was raised:\n{e}\n")
        
    country = "japan"
    try:
        colours = get_colours(flag_colours, country)
        print(f"The flag of {country} has the colors {colours}\n")
    except KeyError as e:
        print(f"A KeyError was raised:\n{e}\n")

    # Task 2B and 2C
    # Tesiting a non existing country
    # 2B explination is done in the function where it is catched
    country = "absurdistan"
    try:
        colours = get_colours(flag_colours, country)
        print(f"The flag of {country} has the colors {colours}\n")
    # Catch the KeyError exception
    except KeyError as e:
        print(f"A KeyError was raised:\n{e}\n")

    # Task 2D
    flagColour = "blue"
    try:
        countries = get_countries(flag_colours, flagColour)
        print(f"Countries with the flag colour {flagColour}:\n{countries}.\n")
    except ValueError as e:
        print(f"A ValueError was raised:\n{e}\n")

    flagColour = "orange"
    try:
        countries = get_countries(flag_colours, flagColour)
        print(f"Countries with the flag colour {flagColour}:\n{countries}.\n")
    except ValueError as e:
        print(f"A ValueError was raised:\n{e}\n")

    # Exercise 3
    print("--- Exercise 3 ---")
    shops = {"extra": {"fish": 90, "bread": 32, "apples": 29, "potatoes": 14},
             "rema": {"fish": 79, "bread": 37, "apples": 39, "milk": 29},
             "spar": {"fish": 85, "bread": 35, "apples": 22, "milk": 38}}
    
    # Testing items that all shops have
    try:
        shoppingList = ["fish", "bread"]
        cheapestShop = find_cheapest_shop(shops, shoppingList)
        print(f"The cheapest shop for buying {shoppingList}:\n{cheapestShop}\n")
    except ValueError as e:
        print(f"A ValueError was raised:\n{e}")

    # Testing items that some shops have
    try:
        shoppingList = ["apples", "milk"]
        cheapestShop = find_cheapest_shop(shops, shoppingList)
        print(f"The cheapest shop for buying {shoppingList}:\n{cheapestShop}\n")
    except ValueError as e:
        print(f"A ValueError was raised:\n{e}")

    # Testin items that no single shop has
    try:
        shoppingList = ["bread", "milk", "potatoes"]
        cheapestShop = find_cheapest_shop(shops, shoppingList)
        print(f"The cheapest shop for buying {shoppingList}:\n{cheapestShop}\n")
    except ValueError as e:
        print(f"A ValueError was raised:\n{e}")

