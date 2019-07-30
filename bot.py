
import constants, base_w
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Contact, KeyboardButton, ChatMember, ChatAction, InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, InlineQueryHandler
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
updater = Updater(token=constants.token)
dispatcher = updater.dispatcher

job_queue = updater.job_queue

count = price = photo = description = title = Socket = adv_0 = adv_1 = delete_t = update_tov = False


def start(bot,update):
    message = update.message
    print(message.chat.id)
    if message.chat.id in constants.admins:
        global count, price, photo, description, title, Socket,adv_0, adv_1, delete_t, update_tov
        bottons = [['Товар','Реклама']]
        text = 'Привет, админ!'
        base_w.delete_none_products()
        count = price = photo = description = title = Socket = adv_0 = adv_1 = delete_t = update_tov = False
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, text, reply_markup=keyboard)
    else:
        base_w.registration(message.chat.id)
        bottons = [['Собрать компьютер/купить комплектующие', 'Мониторы'],
                       ['Компьютерная переферия', 'Мобильные телефоны'], ['Прочая электроника','Компьютеры']]
        keyboard = ReplyKeyboardMarkup(bottons,resize_keyboard=True)
        bot.send_message(message.chat.id, 'Здравствуйте, выберите то что Вас интересует.', reply_markup=keyboard)

def answer_questions(bot,update):
    message = update.message
    if message.chat.id in constants.admins:
        global count, price, photo, description, title, Socket, adv_0, adv_1, delete_t, update_tov
        if message.text == 'Товар':
            bottons = [['Добавить','Удалить'],['Обновить','Домой']]
            text = 'Выберите действие:'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Домой':
            bottons = [['Товар', 'Реклама']]
            text = 'Вы дома'
            base_w.delete_none_products()
            count = price = photo = description = title = Socket = adv_0 = adv_1 = delete_t = update_tov = False
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Добавить':
            bottons = [['Материнская плата','Процессор', 'Оперативная память'],['HDD или SSD','Видеокарта','Охлаждение'],
                       ['Кейс'],['Мониторы'],['Клавиатуры','Мышки','Наушники'], ['Hub, Switch','Принтеры, сканеры, МФУ','Другие'],
                       ['Мобильные телефоны','Прочая электроника'],['Компьютеры'], ['Домой']]
            text = 'Выберите раздел'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Материнская плата':
            bottons = [['Intel', 'AMD'], ['Домой']]
            text = 'Материнская плата'
            base_w.save_type('Материнская плата')
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Intel':
            bottons = [['Socket 775'], ['Socket 1155'], ['Socket 1150'], ['Socket 1151'], ['Socket 1156'],
                       ['Socket 1366'], ['Socket 2011']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Выберите желаемый Socket, в который вы добавите'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'AMD':
            bottons = [['Socket AM4+'], ['Socket TR4'], ['Socket AM4'], ['Socket AM3+'], ['Socket AM3'],
                       ['Socket AM2+'], ['Socket AM2']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Выберите желаемый Socket, в который вы добавите'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Процессор':
            bottons = [['Intеl', 'АMD'], ['Домой']]
            text = 'Процессор'
            base_w.save_type('Процессор')
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Оперативная память':
            bottons = [['DDR 2'], ['DDR 3'], ['DDR 4'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Оперативная память'
            base_w.save_type('Оперативная память')
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'HDD или SSD':
            bottons = [['HDD','SSD'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'HDD или SSD'
            base_w.save_type('HDD или SSD')
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'HDD':
            bottons = [['40Gb-320Gb', '500Gb-1Tb'], ['1Tb-4Tb', '4Tb+'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'HDD'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'SSD':
            bottons = [['20Gb-100Gb','100Gb-300Gb'],['300Gb-500Gb','500Gb+'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'SSD'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Видеокарта':
            bottons = [['1-50$','50-200$'],['200-500$','500+$'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Видеокарта'
            base_w.save_type('Видеокарта')
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Охлаждение':
            bottons = [['1-10$','10-30$'],['30-50$','50+$'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Охлаждение'
            base_w.save_type('Охлаждение')
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Кейс':
            bottons = [['1-20$','20-50$'],['50-100$','100+$'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Кейс'
            base_w.save_type('Кейс')
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Мониторы':
            bottons = [['17"-21"','21"-24"'],['24"-27"','27"+'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Мониторы'
            base_w.save_type('Мониторы')
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Клавиатуры' or message.text =='Мышки' or message.text =='Наушники'\
                or message.text == 'Hub, Switch':
            bottons = [['1-10$', '10-30$'], ['30-50$', '50+$'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text =  message.text
            base_w.save_type(text)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        elif message.text == 'Принтеры, сканеры, МФУ' or message.text =='Другие' or message.text =='Мобильные телефоны'or message.text =='Прочая электроника' or message.text =='Компьютеры':
            bottons = [['Б/У', 'Новое'],['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = message.text
            base_w.save_type(text)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            Socket = True

        #--------------------------------------save--->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif Socket == True:
            Socket = False
            base_w.save_undertype(message.text)
            bottons = [['Домой']]
            text = 'Напишите название продукта'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            title = True

        elif title == True:
            title = False
            base_w.save_title(message.text)
            bottons = [['Домой']]
            text = 'Напишите описание продукта'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            description = True

        elif description == True:
            description = False
            base_w.save_description(message.text)
            bottons = [['Домой']]
            text = 'Пришлите фотографии продукта'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)
            photo = True

        elif photo == True:
            photo = False
            try:
                l = ''
                for i in range(len(message.photo)):
                    l += message.photo[i].file_id + '@#$%$#@'
                base_w.save_photo(l)
                bottons = [['Домой']]
                text ='Ваши фотографии сохранены, пришлите цену продукта'
                keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
                bot.send_message(message.chat.id, text,
                                 reply_markup=keyboard)
                price = True

            except:
                bot.send_message(message.chat.id,
                                 'Произошла ошибка, попробуйте еще раз с самого начала. Убедитесь в правильности данных')
                message.text = 'Домой'
                answer_questions(bot, update)

        elif price == True:
            price = False
            try:
                base_w.save_price(int(message.text))
                bottons = [['Домой']]
                text = 'Пришлите количество продукта на складе'
                keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
                bot.send_message(message.chat.id, text, reply_markup=keyboard)
                count = True
            except:
                bot.send_message(message.chat.id,
                                 'Произошла ошибка, попробуйте еще раз с самого начала. Убедитесь в правильности данных')
                message.text = 'Домой'
                answer_questions(bot, update)

        elif count == True:
            count = False
            try:
                base_w.save_count(int(message.text))
                bottons = [['Домой']]
                text = 'Спасибо, за то что воспользовались именно нашей авиакомпанией!\nНажмите на /start или нажмите кнопку "Домой"'
                keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
                bot.send_message(message.chat.id, text, reply_markup=keyboard)
            except:
                bot.send_message(message.chat.id,
                                 'Произошла ошибка, попробуйте еще раз с самого начала. Убедитесь в правильности данных')
                message.text = 'Домой'
                answer_questions(bot, update)

        #----<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----save--------------------------------------

        #-------------------------------------------------adv---->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif message.text == 'Реклама':
            bottons = [['Фото и текст', 'Только текст'], ['Домой']]
            text = 'Выберите вид рекламы'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Фото и текст':
            text = 'Пришлите фотографии с текстом в описании'
            bottons = [['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text,reply_markup=keyboard)
            adv_0 = True

        elif adv_0 == True:
            adv_0 = False
            try:
                l = ''
                for i in range(len(message.photo)):
                    l += str(message.photo[i].file_id) + '@#$%$#@'
                base_w.adv_photo(l, message.caption)
                buttons = [['Домой']]
                keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
                bot.send_message(message.chat.id,
                                 'Реклама сохранена',
                                 reply_markup=keyboard)
            except:
                bot.send_message(message.chat.id,
                                 'Произошла ошибка, попробуйте еще раз с самого начала. Убедитесь в правильности данных')
                message.text = 'Домой'
                answer_questions(bot, update)

        elif message.text == 'Только текст':
            text = 'Пришлите текст рекламы'
            bottons = [['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text,reply_markup=keyboard)
            adv_1 = True

        elif adv_1 == True:
            adv_1 = False
            base_w.adv_text(message.text)
            bot.send_message(message.chat.id, 'Текст рекламы сохранен')

        #----------------------------------delete->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif message.text == 'Удалить':
            world = base_w.all_tovar_info()
            buttons = [['Домой']]
            keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Выберите номер товара, который хотите удалить:\n'+world, reply_markup=keyboard)
            delete_t = True

        elif delete_t == True:
            delete_t = False
            try:
                base_w.delete_tovar(int(message.text))
                bot.send_message(message.chat.id, 'Товар под номером %s удален' %(message.text))
            except:
                bot.send_message(message.chat.id,
                                 'Произошла ошибка, попробуйте еще раз с самого начала. Убедитесь в правильности данных')
                message.text = 'Домой'
                answer_questions(bot, update)

        elif message.text == 'Обновить':
            world = base_w.all_tovar_info()
            buttons = [['Домой']]
            keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Выберите номер товара, количество которого хотите изменить. И через пробел напишите номер и новое количество товара:\n' + world,
                             reply_markup=keyboard)
            update_tov = True

        elif update_tov == True:
            update_tov = False
            try:
                base_w.update_tovar(message.text.split(' ')[0],message.text.split(' ')[1])
                bot.send_message(message.chat.id, 'Товар под номером %s изменен' %(message.text.split(' ')[0]))
            except:
                bot.send_message(message.chat.id,
                                 'Произошла ошибка, попробуйте еще раз с самого начала. Убедитесь в правильности данных')
                message.text = 'Домой'
                answer_questions(bot, update)

    else:
        # bottons = [['Собрать компьютер/купить комплектующие','Мониторы'],['Компьютерная переферия','Мобильные телефоны'],['Прочая электроника']]
        base_w.last_word(message.chat.id, message.text)
        if message.text == 'Собрать компьютер/купить комплектующие':
            bottons = [['Intel', 'AMD'], ['Далее к разделу "Процессор"','Домой']]
            text = 'Материнская плата'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Домой':
            bottons = [['Собрать компьютер/купить комплектующие', 'Мониторы'],
                       ['Компьютерная переферия', 'Мобильные телефоны'], ['Прочая электроника','Компьютеры'],['Корзина']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Здравствуйте, выберите то что Вас интересует.', reply_markup=keyboard)

        elif message.location != None:
            message_id = message.message_id
            text_list = base_w.price_info(message.chat.id)
            phone = base_w.set_phone(message.chat.id)
            text_ = '---------------------------------------------------------\n'
            sumof = 0
            for i in range(len(text_list)):
                text_ += str(i+1) + '. ' + str(text_list[i][0]) + ' Кол-во: ' + str(
                    text_list[i][1]) + 'шт. Цена за шт: ' + str(text_list[i][2]) + '$ Всего: ' + str(
                    int(text_list[i][2]) * int(text_list[i][1])) + '$\n'
                sumof += (int(text_list[i][2]) * int(text_list[i][1]))
            text_ += '\nИтого: ' + str(sumof) + '$\n\nНомер телефона: +'+str(phone)

            for i in constants.admins:
                try:
                    bot.send_message(chat_id=i, text = text_)
                    bot.forward_message(chat_id=i, from_chat_id=message.chat.id, disable_notification=False,
                                        message_id=message_id)
                except:
                    pass


            bottons = [['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Ваш заказ оформлен. В ближайшее время наш оператор свяжется с вами,\nСпасибо!', reply_markup=keyboard)





        elif message.contact != None:
            contact = update.effective_message.contact
            phone = contact.phone_number
            base_w.update(message.chat.id, phone)
            text_list = base_w.price_info(message.chat.id)
            text_ = ''
            sumof = 0
            for i in range(len(text_list)):
                text_ += str(i+1)+'. '+str(text_list[i][0])+' Кол-во: '+str(text_list[i][1]) + 'шт. Цена за шт: '+str(text_list[i][2])+ '$ Всего: '+ str(int(text_list[i][2])*int(text_list[i][1]))+'$\n'
                sumof += (int(text_list[i][2])*int(text_list[i][1]))
            text_ += '\nИтого: '+str(sumof)+'$'
            con_keyboard = KeyboardButton(text="Отправить местороложение", request_location=True)
            custom_keyboard = [[con_keyboard]]
            keyboard = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Для того, чтобы закончить оформление, пришлите ваше местоположение (нажмите на кнопку)\nИли перейдите в корзину для корректировки /basket\n\n'+text_, reply_markup=keyboard)

        elif message.text.replace('Далее к разделу ','')[0] == '"':
            message.text = message.text.replace('Далее к разделу "', '').replace('"','')
            update.message.text = message.text
            answer_questions(bot,update)

        elif message.text == 'Компьютерная переферия':
            bottons = [['Клавиатуры', 'Мышки', 'Наушники'],['Принтеры, сканеры, МФУ'] ,['Hub, Switch', 'Другие']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = message.text
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Клавиатуры' or message.text =='Мышки' or message.text =='Наушники'\
                or message.text == 'Hub, Switch':
            bottons = [['1-10$', '10-30$'], ['30-50$', '50+$'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text =  message.text
            bot.send_message(message.chat.id, text, reply_markup=keyboard)


        elif message.text == 'Принтеры, сканеры, МФУ' or message.text =='Другие' or message.text =='Мобильные телефоны'or message.text =='Прочая электроника' or message.text =='Компьютеры':
            bottons = [['Б/У', 'Новое'],['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = message.text
            bot.send_message(message.chat.id, text, reply_markup=keyboard)


        elif message.text == 'Intel':
            bottons = [['Socket 775'], ['Socket 1155'], ['Socket 1150'], ['Socket 1151'], ['Socket 1156'],
                       ['Socket 1366'], ['Socket 2011'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Выберите желаемый Socket'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'AMD':
            bottons = [['Socket AM4+'], ['Socket TR4'], ['Socket AM4'], ['Socket AM3+'], ['Socket AM3'],
                       ['Socket AM2+'], ['Socket AM2'],['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Выберите желаемый Socket'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Процессор':
            bottons = [['Intеl', 'АMD'], ['Далее к разделу "Оперативная память"','Домой']]
            text = 'Процессор'
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, text, reply_markup=keyboard)


        elif message.text == 'Оперативная память':
            bottons = [['DDR 2'], ['DDR 3'], ['DDR 4'], ['Далее к разделу "HDD или SSD"','Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Оперативная память'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'HDD или SSD':
            bottons = [['HDD', 'SSD'], ['Далее к разделу "Видеокарта"','Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'HDD или SSD'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)


        elif message.text == 'HDD':
            bottons = [['40Gb-320Gb', '500Gb-1Tb'], ['1Tb-4Tb', '4Tb+'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'HDD'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'SSD':
            bottons = [['20Gb-100Gb', '100Gb-300Gb'], ['300Gb-500Gb', '500Gb+'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'SSD'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Видеокарта':
            bottons = [['1-50$', '50-200$'], ['200-500$', '500+$'], ['Далее к разделу "Охлаждение"','Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Видеокарта'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Охлаждение':
            bottons = [['1-10$', '10-30$'], ['30-50$', '50+$'], ['Далее к разделу "Кейс"','Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Охлаждение'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)


        elif message.text == 'Кейс':
            bottons = [['1-20$', '20-50$'], ['50-100$', '100+$'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Кейс'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Мониторы':
            bottons = [['17"-21"', '21"-24"'], ['24"-27"', '27"+'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = 'Мониторы'
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Клавиатуры' or message.text == 'Мышки' or message.text == 'Наушники' or message.text == 'Hub, Switch':
            bottons = [['1-10$', '10-30$'], ['30-50$', '50+$'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = message.text
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Принтеры, сканеры, МФУ' or message.text == 'Другие' or message.text == 'Мобильные телефоны' or message.text == 'Прочая электроника' or message.text == 'Компьютеры':
            bottons = [['Б/У', 'Новое'], ['Домой']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            text = message.text
            bot.send_message(message.chat.id, text, reply_markup=keyboard)

        elif message.text == 'Корзина':
            message.text = '/basket'
            basket(bot, update)

        elif message.text == 'Очистить корзину':
            base_w.clear_basket(message.chat.id)
            bot.send_message(message.chat.id, 'Корзина очищена')
            message.text ='/start'
            start(bot,update)

        elif message.text.replace('Добавить в корзину','')[0] == ' ':
            title_is = message.text.replace('Добавить в корзину ','')
            id_is = base_w.searching_by_title(title_is)
            count_is = base_w.searching_by_title_1(title_is)
            keyboard = constants.count_bottons(count_is, str(id_is), 0)
            bot.send_message(message.chat.id, 'Выберите количество:', reply_markup=keyboard)

        elif message.text == 'Удалить единицу':
            buttons = [[InlineKeyboardButton('Удалить', switch_inline_query_current_chat='')]]
            keyboard = InlineKeyboardMarkup(buttons)
            bot.send_message(message.chat.id, 'Для продолжения, нажмите на кнопку "Удалить"\nЗатем начните писать название продукта, который хотите удалить', reply_markup=keyboard)

        elif message.text.replace('Вернуться к','')[0] == ' ':
            title_is = message.text.replace('Вернуться к ', '')
            message.text = title_is
            answer_questions(bot, update)

        elif message.text == 'Сборка (5$)':
            id_is = 99999
            count_is = 1
            base_w.save_trash(id_is, count_is, message.chat.id)
            message.text = 'Далее'
            answer_questions(bot, update)

        elif message.text == 'Сборка и установка Windows (9$)':
            id_is = 99998
            count_is = 1
            base_w.save_trash(id_is, count_is, message.chat.id)
            message.text = 'Далее'
            answer_questions(bot,update)

        elif message.text == 'Далее':
            con_keyboard = KeyboardButton(text="Отправить контакт", request_contact=True)
            custom_keyboard = [[con_keyboard]]
            keyboard = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Для продолжения оформления заказа нам нужен ваш номер, для того, чтобы связаться и обсудить детали доставки', reply_markup=keyboard)

        elif message.text == 'Оформить заказ':
            bottons = [['Сборка (5$)','Сборка и установка Windows (9$)'],['Далее']]
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Выберите что-нибудь и дополнительных услуг.\nИли нажмите кнопку "Далее", для продолжения оформления заказа', reply_markup=keyboard)




        else:
            try:
                l = base_w.searching_by(message.chat.id)
                if l[-1] == 'list':
                    bottons = []
                    for i in l[:-1]:
                        bottons.append([i[3]])
                    bottons.append(['Домой'])
                    keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
                    text = 'Выберите продукт:'
                elif l[-1] == 'Product':
                    u_last_word = base_w.parse_ulw(message.chat.id)
                    bottons = [['Добавить в корзину '+l[3]],['Вернуться к '+u_last_word,'Домой']]
                    text = 'Добавьте продукт в корзину\n'+str(l[3])+'\nОписание: '+str(l[4])+'\nЦена: '+str(l[6])+'$'
                    keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
                    bot.send_photo(message.chat.id, photo = l[5].split('@#$%$#')[0] )
                elif l == 'None':
                    text = 'Этот товар в данный момент отсутствует'
                    bottons = [['Домой']]
                    keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
                bot.send_message(message.chat.id, text, reply_markup=keyboard)
            except:
                bot.send_message(message.chat.id, 'Этот товар в данный момент отсутствует')




def delete_(bot, update):
    message = update.message
    try:
        base_w.delete_basket(message.chat.id,int(message.text.split('^')[1]))
        bot.send_message(message.chat.id, 'Товар удален')
        message.text = '/basket'
        basket(bot,update)
    except:
        bot.send_message(message.chat.id, 'Ошибка 404')



def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    else:
        results = []
        id_is = update.inline_query.from_user.id
        nicks = base_w.searching_by_ID(id_is)
        for i in nicks:
            if str(query) in i[0]:
                content = '/delete '+str(i[0])+' ^'+str(i[1])
                results.append(InlineQueryResultArticle(id = id_is, title=str(i[0]),input_message_content=InputTextMessageContent(content)))
    try:
        if results != []:
            bot.answer_inline_query(update.inline_query.id, results)
        else:
            results.append(InlineQueryResultArticle(id='None', title='None',
                                                    input_message_content=InputTextMessageContent(
                                                        'Ничего не найдено\n/start'), description='Ничего не найдено'))
            bot.answer_inline_query(update.inline_query.id, results)
    except:
        pass




def inline_answers(bot, update):
    query = update.callback_query
    if 'Меньше' in str(query.data):
        l = str(query.data).split('Меньше')
        count_is = l[1].split('+')[0]
        id_is = l[1].split('+')[1]
        round_is = l[0]
        bottons = constants.count_bottons(count_is, id_is, round_is)
        keyboard = InlineKeyboardMarkup(bottons)
        bot.edit_message_text(message_id=query.message.message_id ,chat_id=query.message.chat.id,text= 'Выберите количество:', reply_markup=keyboard)
    elif 'Больше' in str(query.data):
        l = str(query.data).split('Меньше')
        count_is = l[1].split('+')[0]
        id_is = l[1].split('+')[1]
        round_is = l[0]
        bottons = constants.count_bottons(count_is, id_is, round_is)
        keyboard = InlineKeyboardMarkup(bottons)
        bot.edit_message_text(message_id=query.message.message_id ,chat_id=query.message.chat.id, text='Выберите количество:', reply_markup=keyboard)

    else:
        count_is = query.data.split('+')[0]
        id_is = query.data.split('+')[1]
        base_w.save_trash(count_is, id_is, query.message.chat.id)
        bot.edit_message_text(message_id=query.message.message_id, chat_id=query.message.chat.id, text='Ваш товар добавлен в корзину\nВызывите команду /basket , чтобы перейти в корзину')

    

def basket(bot,update):
    message = update.message
    info = base_w.info_basket(message.chat.id)
    if info == 'None':
        bot.send_message(message.chat.id, 'Корзина пуста')
        message.text = '/start'
        start(bot, update)
    else:
        text_is = ''
        spisok = info[4:].split('&')[:-1]
        for i in range(len(spisok)):
            text_is += str(i+1)+'. '+base_w.title_from_ID(int(spisok[i].split('+')[0]))+' Кол-во: '+ str(spisok[i].split('+')[1]) +' шт.\n'
        bot.send_message(message.chat.id, 'Корзина:')
        bottons = [['Удалить единицу','Оформить заказ'], ['Очистить корзину'],['Домой']]
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, str(text_is), reply_markup=keyboard)

delete_handler = CommandHandler('delete', delete_)
inline_caps_handler = InlineQueryHandler(inline_caps)
basket_handler = CommandHandler('basket', basket)
start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.all, answer_questions)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(CallbackQueryHandler(inline_answers))
dispatcher.add_handler(basket_handler)
dispatcher.add_handler(answer_handler)
updater.start_polling(timeout=5, clean=True)