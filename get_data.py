import json


def get_aircrafts():
    with open('aircrafts.json', 'r') as aircrafts_file:
        aircrafts = json.load(aircrafts_file)
    return aircrafts
def get_pilots():
    with open('pilots.json', 'r') as pilots_file:
        pilots = json.load(pilots_file)
    return pilots
def get_targets():
    with open('air_strike_targets.json', 'r') as targets_file:
        targets = json.load(targets_file)
    return targets


