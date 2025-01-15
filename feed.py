import api


farmer_udid = "tE6RwldSFcLSQ66x3wmZNw"
ids = {
    "exodawn": {
        "ids": [
            "sky_boss1_rb_1",
            "sky_boss1_rb_2",
            "sky_boss1_rb_3",
            "sky_boss1_rb_4",
            "sky_boss1_rb_5"
        ],
        "per_id": 5
    }
}


def feed_all(event_id):
    inventory = api.inventory(farmer_udid)
    if (inventory is None):
        return "ERROR"
    if (len(inventory["monster_inventory"]["monsters"]) - 5 < len(ids[event_id]["ids"]) * ids[event_id]["per_id"]):
        return "Not enough mobs now, please try again later..."
    to_feed = [[] for i in range(len(ids[event_id]["ids"]))]
    index = 0
    for monster in inventory["monster_inventory"]["monsters"]:
        if (monster["id"] != "kitsune"):
            continue
        to_feed[index].append(monster["inventory_id"])
        if (len(to_feed[index]) == ids[event_id]["per_id"]):
            index += 1
        if (index == len(ids[event_id]["ids"])):
            break
    for i in range(len(to_feed)):
        try:
            api.monster_event_donate(to_feed[i], farmer_udid, ids[event_id]["ids"][i])
        except:
            return "ERROR"
    return "SUCCESS"
