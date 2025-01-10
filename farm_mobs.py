import api
import string, random
import time


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


farmer_udid = "dn7RR6j578qJgxNlMlESuA"
farmer_token = "kw5fmf"
while True:
    inventory = api.inventory(farmer_udid)
    if (inventory is None):
        continue
    if (len(inventory["monster_inventory"]["monsters"]) < 305):
        for i in range(80):
            try:
                create_account(farmer_token)
            except:
                pass
    time.sleep(10)
