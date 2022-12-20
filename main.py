import telebot
import random

from env import TOKEN

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Yes')
button2 = telebot.types.KeyboardButton('No')
keyboard.add(button1,button2)





@bot.message_handler(commands=['start','hi'])
def start_function(message):
    msg = bot.send_message(message.chat.id,f'Hello {message.chat.first_name} start the game?',
    reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer_check)
#     bot.send_sticker(message.chat.id,'CAACAgEAAxkBAAJKHmOhPWSNwVM5PkZIIdcX7EoQGRoDAALAAQACoKm5LKF3viyr6QbzLAQ')
# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text)

def answer_check(msg):
    if msg.text == 'Yes':
        bot.send_message(msg.chat.id, 'you have 3 chanses to choose number from 1 till 10')
        random_number = random.randint(1,10)
        p = 3
        start_game(msg,random_number,p)

    else:
        bot.send_message(msg.chat.id, 'Okay')

def start_game(msg, random_number,p):
    msg = bot.send_message(msg.chat.id, 'Input number from 1 to 10: ')
    bot.register_next_step_handler(msg, check_func, random_number, p=p-1)


def check_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id, 'Win!')
    elif p == 0:
        bot.send_message(msg.chat.id ,f'Lose! The number was {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Try again you have {p} tryes')
        start_game(msg, random_number,p)

bot.polling()