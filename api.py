import json
import requests
import string
import random
import copy

account = open("account.json")
create_account_data = json.load(account)
account.close()

referral_code_file = open("referral_code.json")
referral_code_data = json.load(referral_code_file)
referral_code_file.close()

inventory_file = open("inventory.json")
inventory_data = json.load(inventory_file)
inventory_file.close()

decr_energy_file = open("decr_energy.json")
decr_energy_data = json.load(decr_energy_file)
decr_energy_file.close()

battle_won_file = open("battle_won.json")
battle_won_data = json.load(battle_won_file)
battle_won_file.close()

miss_out_file = open("miss_out.json")
miss_out_data = json.load(miss_out_file)
miss_out_file.close()

request_room_file = open("request_room.json")
request_room_data = json.load(request_room_file)
request_room_file.close()

character_update = open("character_update.json")
character_update_data = json.load(character_update)
character_update.close()

finished_tutorial = open("finished_tutorial.json")
finished_tutorial_data = json.load(finished_tutorial)
finished_tutorial.close()

init = open("init.json")
init_data = json.load(init)
init.close()

register_push = open("register_push.json")
register_push_data = json.load(register_push)
register_push.close()

event_donate = open("monster_event_donate.json")
event_donate_data = json.load(event_donate)
event_donate.close()

url = "http://battlecamp.com/api/"
headers = {'User-Agent': 'Monsters/a.5.34.0'}


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


def get_token():
    token = ""
    letters = string.ascii_letters + "0123456789"
    token += "".join(random.choice(letters) for i in range(11))
    letters += "-_"
    token += "".join(random.choice(letters) for i in range(140))
    return token


def create_bot(name):
    new_data = copy.copy(create_account_data)
    new_data["login"] = name
    new_data["email"] = new_data["email"].replace("NULL", name)
    response_create = requests.post(url + "register_email", json=new_data, headers=headers)
    if (response_create.json()["status_code"] != 0):
        return None
    udid = response_create.json()["udid"]
    new_init = init_data
    new_init["udid"] = udid
    response_init = requests.post(url + "init", json=new_init, headers=headers)
    new_register_push = register_push_data
    new_register_push["udid"] = udid
    new_register_push["token"] = get_token()
    response_register = requests.post(url + "register_push", json=new_register_push, headers=headers)
    return udid


def finished_tutorial_do(udid):
    new_finished_tutorial_data = finished_tutorial_data
    new_finished_tutorial_data["udid"] = udid
    response_finished_tutorial = requests.post(url + "finished_tutorial", json=new_finished_tutorial_data, headers=headers)
    if (response_finished_tutorial.json()["status_code"] != 0):
        return None
    return True


def request_room(udid, place, place_codename):
    new_request_room_data = request_room_data
    new_request_room_data["udid"] = udid
    new_request_room_data["place"] = place
    new_request_room_data["place_codename"] = place_codename
    response_request_room = requests.post(url + "request_room", json=new_request_room_data, headers=headers)
    if (response_request_room.json()["status_code"] != 0):
        return None
    return response_request_room.json()


def character_updating(event_id, udid, place):
    new_character_update = character_update_data
    new_character_update["udid"] = udid
    new_character_update["event_id"] = event_id
    new_character_update["place"] = place
    response_character_update = requests.post(url + "monster_character_update", json=new_character_update, headers=headers)
    if (response_character_update.json()["status_code"] != 0):
        return None
    return True


def decr_energy(udid, count=5):
    new_decr_energy = copy.copy(decr_energy_data)
    new_decr_energy["udid"] = udid
    new_decr_energy["amount"] = count
    response_decr_energy = requests.post(url + "monster_decr_energy", json=new_decr_energy, headers=headers)
    if (response_decr_energy.json()["status_code"] != 0):
        return None
    return response_decr_energy.json()["battle_id"]


def story_respond(udid, id):
    new_story_respond = copy.copy(story_respond_data)
    new_story_respond["udid"] = udid
    new_story_respond["id"] = id
    response_story_respond= requests.post(url + "monster_story_respond", json=new_story_respond, headers=headers)
    if (response_story_respond.json()["status_code"] != 0):
        return 0
    print(id)
    return response_story_respond.json()["xp"]["level"]


def miss_out():
    response_gacha_info = requests.post(url + "miss_out", json=miss_out_data, headers=headers)
    print(response_gacha_info.json())


def battle_won(udid, battle_id):
    new_battle_won = copy.copy(battle_won_data)
    new_battle_won["udid"] = udid
    new_battle_won["battle_id"] = battle_id
    response_battle_won = requests.post(url + "monster_battle_won", json=new_battle_won, headers=headers)
    if (response_battle_won.json()["status_code"] != 0):
        return None
    return response_battle_won.json()["xp"]["level"]


def inventory(udid):
    new_inventory = copy.copy(inventory_data)
    new_inventory["udid"] = udid
    response_inventory = requests.post(url + "monster_inventory", json=new_inventory, headers=headers)
    if ("status_code" not in response_inventory.json().keys() or response_inventory.json()["status_code"] != 0):
        return None
    return response_inventory.json()


def monster_event_donate(monsters, udid, event_id):
    new_event_donate = copy.copy(event_donate_data)
    new_event_donate["udid"] = udid
    new_event_donate["monsters"] = monsters
    new_event_donate["event_id"] = event_id
    response_event_donate = requests.post(url + "monster_event_donate", json=new_event_donate, headers=headers)
    if ("status_code" not in response_event_donate.json().keys() or response_event_donate.json()["status_code"] != 0):
        return None
    return response_event_donate.json()


def referral_code(udid, code):
    new_referral_code = copy.copy(referral_code_data)
    new_referral_code["udid"] = udid
    new_referral_code["code"] = code
    response_inventory = requests.post(url + "monster_referral_code", json=new_referral_code, headers=headers)

