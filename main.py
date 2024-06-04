import telebot
from telebot import types
from datetime import date
import requests, json, webbrowser
import Parse

TOKEN = '5247832216:AAE21z1COSSrVZwnifZSBg0P15ajOSLM5Iw'
bot = telebot.TeleBot(TOKEN)
# api key = 22d0948b-0e64-41dd-953e-23a94e5e7bd0

d1={'Нур-Султан':'c163',
    'Астана':'c163',
   'Алматы':'c22177',
   'Атырау':'c10291',
   'Караганды':'c164',
   'Кызылорда':'c21050',
   'Шымкент':'c22176',
   'Петропавловск':'c22193',
   'Кокшетау':'c22172',
   'Костанай':'c10295',
   'Актобе':'c20273',
   'Тараз':'c21094',
   'Семей':'c165',
   'Усть-Каменогорск':'c10306',
   'Туркестан':'c21106',
   'Талдыкорган':'c10303',
   'Экибастуз':'c23184',
   'Актау':'c10286',
   'Уральск':'c42434',
   'Павлодар':'c190'}

d2={'Нур-Султан':'2708001',
    'Астана':'2708001',
   'Алматы':'2700000',
   'Атырау':'2704830',
   'Караганды':'2708952',
   'Кызылорда':'2704999',
   'Шымкент':'2700770',
   'Петропавловск':'2040500',
   'Кокшетау':'2708803',
   'Костанай':'2708700',
   'Актобе':'2704600',
   'Тараз':'2700710',
   'Семей':'2700900',
   'Усть-Каменогорск':'2700890',
   'Туркестан':'2700860',
   'Талдыкорган':'2700108',
   'Экибастуз':'2708021',
   'Актау':'2708905',
   'Уральск':'2704810',
   'Павлодар':'2708900'
}

# url = "https://api.rasp.yandex.net/v3.0/search/?apikey=22d0948b-0e64-41dd-953e-23a94e5e7bd0&format=json&from=c146&to=c213&lang=ru_RU&page=1&date=2022-06-23&transport_types=train"
# res = .get(url)

@bot.message_handler(commands=['test'])
def handler_test(message):
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Новости 🌏')
    item2 = types.KeyboardButton('История ЖД 🚂')
    item3 = types.KeyboardButton('Контакты "Темір жол" ☎')
    item4 = types.KeyboardButton('Популярные рейсы 🥇')

    markup.add(item1, item2, item3,item4)

    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name} {0.last_name}, введите "/info" для получение инструкции по основной фукнции бота или вы можете узнать список доступных городов по команде "/lst".'
                                      ' Также можно получить список сайтов по продаже билетов используя "/sites"' +
                                    'Если не ввести дату рейса, рейсы по заданным пунктам будут находится за текущее число.'.format(message.from_user),reply_markup=markup)
    img = open('Train.gif', 'rb')
    bot.send_animation(message.chat.id, img)

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.from_user.id, "Введите ваш путь в виде:' + '\n' + (Путь Город1 Город2 Дату(Год-месяц-число))" + "\n" +
                     "Например: (Путь Алматы Нур-Султан 2022-05-02)" + "\n" +
                     'Cейчас доступны в основном крупные города Казахстана, список городов можно найти по команде "/lst"')

@bot.message_handler(commands=['lst'])
def lst(message):
    img1 = open('Список.png', 'rb')
    bot.send_photo(message.chat.id, img1)
    bot.send_message(message.from_user.id, 'По вышеперчисленным городам можно найти рейсы. Поиск рейсов осуществляется в виде ввода сообщения'+'\n'+
                     'Путь Город1 Город2 Дату(Год-месяц-число)' + '\n' +
                     'Если не ввести дату рейса, рейсы по заданным пунктам будут находится за текущее число.')


@bot.message_handler(commands=['sites'])
def sites(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Bilet.RailWays.kz')
    item2 = types.KeyboardButton('Aviata.kz')
    item3 = types.KeyboardButton('Tickets.kz')
    item4 = types.KeyboardButton('Назад 🔙')

    markup.add(item1, item2, item3,item4)

    bot.send_message(message.chat.id, 'Вот меню сайтов:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    try:
        if message.chat.type == 'private':
            print(message.text)
            print(list(str(message.text))[0])
            text = str(message.text).lower()
            # if list(str(message.text))[0] == 'путь' or 'Путь':
            if 'путь' in str(text).lower():
                p = str(date.today())
                if len(str(text).split()) == 4:
                    x, y, z, p = str(text).lower().title().split()
                else:
                    x, y, z = str(text).lower().title().split()
                for i in d1:
                    if y == i:
                        y1 = d2[y]
                        y = d1[y]
                    if z == i:
                        z1 = d2[z]
                        z = d1[z]
                pf = ".".join(p.split(sep='-')[::-1])
                url = "https://api.rasp.yandex.net/v3.0/search/?apikey=22d0948b-0e64-41dd-953e-23a94e5e7bd0&format=json&from={0}&to={1}&lang=ru_RU&page=1&date={2}&transport_types=train".format(
                    y, z, p)
                url1 = "https://aviata.kz/railways/search?station_from={0}&station_to={1}&departure_date={2}".format(y1,z1,pf)
                res = requests.get(url)
                print(res.text)
                total = (res.json()['pagination']['total'])
                if total ==0:
                    bot.send_message(message.from_user.id, 'Нет прямого рейса по заданным параметрам')
                for i in range(int (total)):
                    bot.send_message(message.from_user.id, str(
                        res.json()['segments'][i]['thread']['title'] + '\n' +
                        res.json()['segments'][i]['departure'] + ' ' + '\n' +
                        res.json()['segments'][i]['from']['title'] + '\n' + '\n' +
                        res.json()['segments'][i]['thread']['carrier']['contacts']) + '\n' + '\n' + url1)

            elif message.text == 'Bilet.RailWays.kz' in message.text:
                click.launch('https://bilet.railways.kz/')
            elif message.text == 'Aviata.kz' in message.text:
                webbrowser.open('https://aviata.kz/railways/')
            elif message.text == 'Tickets.kz' in message.text:
                webbrowser.open('https://tickets.kz/gd')
            elif message.text == 'Новости 🌏' in message.text:
                bot.send_message(message.from_user.id, 'https://railways.kz/articles/company/news')
            elif message.text == 'История ЖД 🚂' in message.text:
                bot.send_message(message.from_user.id, 'https://railways.kz/articles/company/istoriya')
            elif message.text == 'Контакты "Темір жол" ☎' in message.text:
                bot.send_message(message.from_user.id, 'https://railways.kz/articles/contacts')
            elif message.text == 'Популярные рейсы 🥇' in message.text:
                handler_test(message)
                bot.send_message(message.from_user.id, Parse.get_content() + '\nОзнакомится с предложениями можно по ссылке: \nhttps://aviata.kz/railways/#')
            elif message.text == 'Назад 🔙' in message.text:
                handler_test(message)
                start(message)
    except Exception:
        bot.send_message(message.from_user.id, "Некорректный ввод")


bot.polling(none_stop=True)
# ИЗМЕНЕНИЯ РАДИ АДЕЛИ

# ASTANA

# NUR - SULTAN