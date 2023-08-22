from bs4 import BeautifulSoup
import requests
import json

# Get api key
def getKey():
    key = 'D:\PYTHON\steamProject\key.txt'
    with open(key, 'r') as file:
        key = file.read()
        return key

# Get games from api
def getUserGames(steamId):
    games = []
    steamPage = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={getKey()}&steamid={steamId}&include_appinfo=True&format=json'
    user = BeautifulSoup(requests.get(steamPage).text, 'html.parser')  # send request to page using beautiful soup
    data = json.loads(user.text)['response']['games']
    for i in data:
        games.append(i['name'])

    return games

# Add games to txt file
def generateFile(steamId):
    file = open("steamgames.txt", "w")
    for game in getUserGames(steamId):
        file.write(game + "\n")

