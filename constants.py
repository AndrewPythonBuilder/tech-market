a = """    if message.text == 'Собрать компьютер/купить комплектующие':
            text = 'Выберите тип материнской платы'
            bottons = [['Intel','AMD'], ['Далее']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Intel':
            bottons = [['Socket 775'], ['Socket 1155'], ['Socket 1150'], ['Socket 1151'], ['Socket 1156'],
                       ['Socket 1366'], ['Socket 2011']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Выберите желаемый Socket'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'AMD':
            bottons = [['Socket AM4+'], ['Socket TR4'], ['Socket AM4'], ['Socket AM3+'], ['Socket AM3'],
                       ['Socket AM2+'], ['Socket AM2']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Выберите желаемый Socket'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Далее':
            text = 'Выберите желаемый процессор'
"""

import logging
import  base_w
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Contact, KeyboardButton, ChatMember, ChatAction, InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, InlineQueryHandler

token = '945681496:AAHU82-D0Oee9aXkV_8S9aEIMbDZg4IOklU'


admins = [286077227]

sokets = ['Socket 775', 'Socket 1155', 'Socket 1150', 'Socket 1151', 'Socket 1156','Socket 1366', 'Socket 2011', 'Socket AM4+', 'Socket TR4', 'Socket AM4', 'Socket AM3+', 'Socket AM3','Socket AM2+', 'Socket AM2']

def count_bottons(coun, requests, round):
    if coun % 10 == 1:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round))]]
    elif coun % 10 == 2:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round))]]
    elif coun % 10 == 3:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)), InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))]]
    elif coun % 10 == 4:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],[InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round))]]
    elif coun % 10 == 5:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],[InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round)),InlineKeyboardButton(text = str(5+round), callback_data = requests+'+'+str(5+round))]]
    elif coun % 10 == 6:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],
               [InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round)), InlineKeyboardButton(text = str(5+round), callback_data = requests+'+'+str(5+round)),InlineKeyboardButton(text = str(6+round), callback_data = requests+'+'+str(6+round))]]
    elif coun % 10 == 7:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],
               [InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round)), InlineKeyboardButton(text = str(5+round), callback_data = requests+'+'+str(5+round)),
                InlineKeyboardButton(text = str(6+round), callback_data = requests+'+'+str(6+round))],[InlineKeyboardButton(text = str(7+round), callback_data = requests+'+'+str(7+round))]]
    elif coun % 10 == 8:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],
               [InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round)), InlineKeyboardButton(text = str(5+round), callback_data = requests+'+'+str(5+round)),
                InlineKeyboardButton(text = str(6+round), callback_data = requests+'+'+str(6+round))],[InlineKeyboardButton(text = str(7+round), callback_data = requests+'+'+str(7+round)),InlineKeyboardButton(text = str(8+round), callback_data = requests+'+'+str(8+round))]]
    elif coun % 10 == 9:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],
               [InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round)), InlineKeyboardButton(text = str(5+round), callback_data = requests+'+'+str(5+round)),
                InlineKeyboardButton(text = str(6+round), callback_data = requests+'+'+str(6+round))],
               [InlineKeyboardButton(text = str(7+round), callback_data = requests+'+'+str(7+round)), InlineKeyboardButton(text = str(8+round), callback_data = requests+'+'+str(8+round)),InlineKeyboardButton(text = str(9+round), callback_data = requests+'+'+str(9+round))]]
    elif coun % 10 == 0:
        ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],
               [InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round)), InlineKeyboardButton(text = str(5+round), callback_data = requests+'+'+str(5+round)),
                InlineKeyboardButton(text = str(6+round), callback_data = requests+'+'+str(6+round))],
               [InlineKeyboardButton(text = str(7+round), callback_data = requests+'+'+str(7+round)), InlineKeyboardButton(text = str(8+round), callback_data = requests+'+'+str(8+round)),
                InlineKeyboardButton(text = str(9+round), callback_data = requests+'+'+str(9+round))],
               [InlineKeyboardButton(text ='Больше',callback_data = str(round+10)+'Больше'+str(coun)+'+'+str(requests)),
                InlineKeyboardButton(text = str(10+round), callback_data = requests+'+'+str(10+round))]]


        if round != 0:
            ret[-1].append(InlineKeyboardButton(text='Меньше',callback_data=str(round-10)+'Меньше'+str(coun)+'+'+str(requests)))
        else:
            ret[-1].append(InlineKeyboardButton(text='      ',callback_data=str('None')))

        if round == coun:
            ret = [[InlineKeyboardButton(text = str(1+round), callback_data = requests+'+'+str(1+round)), InlineKeyboardButton(text = str(2+round), callback_data = requests+'+'+str(2+round)),
                InlineKeyboardButton(text = str(3+round), callback_data = requests+'+'+str(3+round))],
               [InlineKeyboardButton(text = str(4+round), callback_data = requests+'+'+str(4+round)), InlineKeyboardButton(text = str(5+round), callback_data = requests+'+'+str(5+round)),
                InlineKeyboardButton(text = str(6+round), callback_data = requests+'+'+str(6+round))],
               [InlineKeyboardButton(text = str(7+round), callback_data = requests+'+'+str(7+round)), InlineKeyboardButton(text = str(8+round), callback_data = requests+'+'+str(8+round)),
                InlineKeyboardButton(text = str(9+round), callback_data = requests+'+'+str(9+round))],[InlineKeyboardButton(text = str(10+round), callback_data = requests+'+'+str(10+round))]]

    if coun % 10 != 0:
        if round != 0:
            ret.append([InlineKeyboardButton(text='Меньше',callback_data= str(round-10)+'Меньше'+str(coun)+'+'+str(requests))])

    bottons = ret
    keyboard = InlineKeyboardMarkup(bottons)
    
    return keyboard
