import time
import requests
from dotenv import load_dotenv
import os
import telebot

load_dotenv()


url = os.environ.get("URL")
token = os.environ.get("TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(["start"])
def start(message):
    value = get_result()
    bot.reply_to(message, f"{value}")


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["data"]
        return data
    # print(len(data["data"])) #698


def get_result():
    oldstore = []
    newstore = []
    oldstore = get_data(url)
    while True:
        res = []
        newstore = get_data(url)
        new_objects = [obj for obj in newstore if obj not in oldstore]

        # Print newly added objects
        if new_objects:
            print("Newly listing Detected:")
            for obj in new_objects:
                res.append(obj)
                oldstore = newstore
            return res
        print("printed.")
        time.sleep(3600)


bot.polling()
