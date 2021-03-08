import telebot
from time import sleep
from telebot import types
import threading
from datetime import datetime


bot = telebot.TeleBot("1604632356:AAFHENBIdh7tj4BuXqJHQYmuACVqxO_o1xA", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to 1702ai Bot for your security!")

def start():
    global message1
    global photo1
    global video1

    message1 = bot.send_message('-1001164801129', '!!!!!!!!!!ALERT!!!!!!!!')

    photo = open('Data/gun.jpg', 'rb')
    photo1 = bot.send_photo('-1001164801129', photo)

    video = open('Data/vid.mp4', 'rb')
    video1 = bot.send_video('-1001164801129', video)

def take_input():
    global message2
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard = True)
    itembtn1 = types.KeyboardButton('yes')
    itembtn2 = types.KeyboardButton('no')
    markup.add(itembtn1, itembtn2)
    message2 = bot.send_message('-1001164801129', "Is this a correct alert?", reply_markup=markup)

start()

take_input()



updates = bot.get_updates(1234,100,5)
updx = updates[0]


@bot.message_handler(regexp="yes")
def handle_message(message):
    global message3
    markup = types.ReplyKeyboardMarkup(selective=True, row_width=1, one_time_keyboard=True)
    itembtn3 = types.KeyboardButton('undo')
    markup.add(itembtn3)

    current_datetime = datetime.now()
    print(current_datetime)
    message3 = bot.send_message('-1001164801129','Alerting the Police at ' + str(current_datetime) , reply_markup=markup)
    send_to_others()

    @bot.message_handler(regexp="undo")
    def handle_message(message):
        bot.send_message('-553512702', 'Alert Retreated!!')

    threading.Timer(5,delete_messages_yes).start()

def delete_messages_yes():
    # sleep(3)
    bot.delete_message(chat_id='-1001164801129', message_id = message1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = photo1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = video1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = message2.message_id)
    # bot.delete_message(chat_id='-1001164801129', message_id = message3.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id=updx.message.message_id)
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message('-1001164801129','Alert successfully completed!', reply_markup = markup)

@bot.message_handler(regexp="no")
def handle_message(message):
    global message4
    markup = types.ReplyKeyboardMarkup(selective=True, row_width=1, one_time_keyboard=True)
    itembtn3 = types.KeyboardButton('undo')
    markup.add(itembtn3)
    message4 = bot.send_message('-1001164801129','Okay, False Alarm!',reply_markup=markup)

    @bot.message_handler(regexp="undo")
    def handle_message(message):
        current_datetime = datetime.now()
        print(current_datetime)
        bot.send_message('-1001164801129', 'Alerting the Police at ' + str(current_datetime))
        send_to_others()

    threading.Timer(5,delete_messages_no).start()

def delete_messages_no():
    sleep(3)
    bot.delete_message(chat_id='-1001164801129', message_id = message1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = photo1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = video1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = message2.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = message4.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id=updx.message.message_id)
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message('-1001164801129', 'Alert successfully completed!', reply_markup=markup)


def send_to_others():
    bot.forward_message('-553512702', '-1001164801129', message1.message_id)
    bot.forward_message('-553512702', '-1001164801129', photo1.message_id)
    bot.forward_message('-553512702', '-1001164801129', video1.message_id)


def delete_messages_anyways():
    sleep(3)
    bot.delete_message(chat_id='-1001164801129', message_id = message1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = photo1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = video1.message_id)
    bot.delete_message(chat_id='-1001164801129', message_id = message2.message_id)

threading.Timer(600,delete_messages_anyways).start()
bot.polling()
