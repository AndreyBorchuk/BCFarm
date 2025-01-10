import telebot
import time
from BCFarmer.feed import feed_all

token = "7744334822:AAFhDyml21rbAHhl5NwWK3Yd6SsbW_nmd0M"
bot = telebot.TeleBot(token)


event_id = "exodawn"
last_req = 0


@bot.message_handler(content_types=['text'])
def farm(message):
    global last_req
    if (message != "farm-rebels"):
        return 0
    if (last_req + 90 > time.time()):
        bot.send_message(message.chat.id, text="Please wait 1.5 minute after previous request")
        return 0
    bot.send_message(message.chat.id, text=feed_all("exodawn"))
    last_req = time.time()


bot.polling(none_stop=True, interval=0)