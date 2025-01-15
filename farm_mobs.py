import api
import string, random
import time, json


def get_state(key):
    states_file = open("data\statuses.json")
    states = json.load(states_file)
    states_file.close()
    return states[key]


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


def create_account(token):
    udid = api.create_bot(get_random_name())
    if (udid is None):
        print("Error while creating account")
        return 0
    status = api.request_room(udid, "playcamp", "playcamp")
    if (status is None):
        print("Error while request room")
        return 0
    api.referral_code(udid, token)
    print(1)


farmer_udid = "tE6RwldSFcLSQ66x3wmZNw"
farmer_token = "2vucu"
while True:
    inventory = api.inventory(farmer_udid)
    if inventory is None:
        continue
    if len(inventory["monster_inventory"]["monsters"]) < 355 and get_state("is_farm") == True:
        for i in range(80):
            create_account(farmer_token)
    time.sleep(10)
