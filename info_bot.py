import telebot
import time, json
from feed import feed_all

token = "7744334822:AAFhDyml21rbAHhl5NwWK3Yd6SsbW_nmd0M"
bot = telebot.TeleBot(token)


last_req = 0
events_file = open("data\events.json")
event_ids = json.load(events_file).keys()
events_file.close()


def get_state(key):
    states_file = open("data\statuses.json")
    states = json.load(states_file)
    states_file.close()
    return states[key]


def set_state(key, state):
    states_file = open("data\statuses.json")
    states = json.load(states_file)
    states_file.close()
    states_file = open("data\statuses.json", "w")
    states[key] = state
    json.dump(states, states_file, indent=4)
    states_file.close()
    return True


@bot.message_handler(commands=["start"])
def farm(message):
    global last_req
    if (last_req + 45 > time.time()):
        bot.send_message(message.chat.id, text="Please wait 45 secs after previous request")
        return 0
    if get_state("is_farm") == True:
        bot.send_message(message.chat.id, text="Bot already accumulating mobs")
        return 0
    set_state("is_farm", True)
    bot.send_message(message.chat.id, text="Bot starting...")
    last_req = time.time()

@bot.message_handler(commands=["stop"])
def stop_farm(message):
    global last_req
    if (last_req + 45 > time.time()):
        bot.send_message(message.chat.id, text="Please wait 45 secs after previous request")
        return 0
    if get_state("is_farm") == False:
        bot.send_message(message.chat.id, text="Bot not started")
        return 0
    set_state("is_farm", False)
    bot.send_message(message.chat.id, text="Bot stopping...")
    last_req = time.time()

@bot.message_handler(commands=["feed"])
def feed(message):
    global last_req
    if (last_req + 45 > time.time()):
        bot.send_message(message.chat.id, text="Please wait 45 secs after previous request")
        return 0
    if get_state("is_farm") == True:
        bot.send_message(message.chat.id, text="You can't feed, please stop bot before do that...")
        return 0
    bot.send_message(message.chat.id, text=feed_all("exodawn"))
    last_req = time.time()


@bot.message_handler(commands=["set"])
def feed(message):
    global last_req
    if (last_req + 45 > time.time()):
        bot.send_message(message.chat.id, text="Please wait 45 secs after previous request")
        return 0
    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, text="Usage: /set {event_id}")
        return 0
    if message.text.split()[1] not in event_ids:
        bot.send_message(message.chat.id, text="Undefined event id")
        return 0
    set_state("event_id", message.text.split()[1])
    bot.send_message(message.chat.id, text=f"Event id setted to: {message.text.split()[1]}")
    last_req = time.time()

bot.polling(none_stop=True, interval=0)