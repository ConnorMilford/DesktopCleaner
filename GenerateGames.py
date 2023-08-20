from bs4 import BeautifulSoup
import requests
import json


def getKey():
    key = 'D:\PYTHON\steamProject\key.txt'
    with open(key, 'r') as file:
        key = file.read()
        return key


def getUserGames(steamId):
    games = []
    steamPage = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={getKey()}&steamid={steamId}&include_appinfo=True&format=json'
    user = BeautifulSoup(requests.get(steamPage).text, 'html.parser')  # send request to page using beautiful soup
    data = json.loads(user.text)['response']['games']
    for i in data:
        games.append(i['name'])

    return games


def generateFile(steamId):
    file = open("steamgames.txt", "w")
    for game in getUserGames(steamId):
        file.write(game + "\n")


generateFile(76561198346676755)
