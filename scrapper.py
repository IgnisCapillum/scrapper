import steammarket as sm
import json
import requests
import time

def parse(item):
    return(sm.get_csgo_item(item)["lowest_price"])

def parseInventory(steam64):
    json_data = (requests.get("https://steamcommunity.com/profiles/"+steam64+"/inventory/json/730/2")).json()
    descriptions = json_data["rgDescriptions"]
    for item in descriptions:
        time.sleep(1)
        name = descriptions[item]["market_hash_name"]
        print(name + " - " + parse(name))


parseInventory("76561199016611800")