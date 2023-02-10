import requests


def get_drink_data(a):
    api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

    get_data = requests.get(api_url + a).json()

    if get_data["drinks"] == None:
        return False
    else:
        return True


class DrinkInfo:
    def __init__(self, drink):
        self.drink = drink

    def thumb(self):
        api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

        get_data = requests.get(api_url + self.drink).json()

        return get_data["drinks"][0]["strDrinkThumb"]

    def tags(self):
        api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

        get_data = requests.get(api_url + self.drink).json()

        return get_data["drinks"][0]["strTags"]

    def instructions(self):
        api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

        get_data = requests.get(api_url + self.drink).json()

        return get_data["drinks"][0]["strInstructions"]
