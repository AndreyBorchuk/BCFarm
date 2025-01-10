import json
import time
import api
from threading import Thread
import string
import random

import info_bot

epic_ids = open("epic_ids", "r").read().split("\n")
print(epic_ids)


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


while (True):
    try:
        udid = api.create_bot(get_random_name())
        if (udid is None):
            print("Error while creating account")
            continue
        print(str(n) + "\t" + udid)
        n += 1
        status = api.settings_do(udid)
        if (status is None):
            print("Error while settings")
            continue
        status = api.request_room(udid, "playcamp", "playcamp")
        if (status is None):
            print("Error while request room")
            continue
        api.referral_code(udid, "p5licd")

    except:
        print("ERROR??")