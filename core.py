# pip install pyTelegramBotAPI документация на pypi
import telebot

# модуль обработки для фото, видео, аудио
from telebot import types

# сам токен в файле config.py
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

# главное меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🔎 roadmap 🔍')
    item2 = types.KeyboardButton('📩 новости мира IT 📩')
    item3 = types.KeyboardButton('👾 тесты  и стикер 👾')
    item4 = types.KeyboardButton('🎯 вопрос о сотрудничестве 🎯')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Хай, {0.first_name}!'.format(message.from_user), reply_markup=markup)

# функционал кнопок главного меню
@bot.message_handler(content_types=['text','photo','site', 'website'])
def bot_message(message):
    if message.chat.type == 'private':

        if message.text == '🔎 roadmap 🔍':
            bot.send_message(message.chat.id, 'Роадмап')
            file = open('./static/roadmap.png', 'rb')
            bot.send_photo(message.chat.id, file)

        elif message.text == '👾 тесты  и стикер 👾':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🔝 тесты 🔝')
            item2 = types.KeyboardButton('🔋 алго-задачи 🔋')
            item3 = types.KeyboardButton('👽 стикер 👽')
            back = types.KeyboardButton('⬅️ назад')
            markup.add(back, item1, item2, item3)
            bot.send_message(message.chat.id, '👾 тесты  и стикер 👾', reply_markup=markup)

        elif message.text == '📩 новости мира IT 📩':
            markup = types.InlineKeyboardMarkup()

            # надо поменять ссылку на новостную страницу сайта

            btn = types.InlineKeyboardButton('Все свежие новости мира IT', url='https://habr.com/ru/news/')
            markup.row(btn)
            bot.reply_to(message, 'Чекай актуалочки  ⬇️', reply_markup=markup)

        elif message.text == '🎯 вопрос о сотрудничестве 🎯':
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Пишите в лс', url='https://t.me/developing_backend')
            markup.row(btn)
            bot.reply_to(message, 'Будем рады предложениям✊🏼', reply_markup=markup)

        elif message.text == '🔝 тесты 🔝':
            markup = types.InlineKeyboardMarkup()

            # надо поменять ссылку на вкладку тестов сайта

            btn = types.InlineKeyboardButton('Перейдите по ссылке для решения тестов', url='https://tproger.ru/quiz/python-beginner')
            markup.row(btn)
            bot.reply_to(message, 'Хороший выбор🧚🏻‍♀️', reply_markup=markup)

        elif message.text == '🔋 алго-задачи 🔋':
            markup = types.InlineKeyboardMarkup()

            # надо поменять ссылку на вкладку сайта

            btn = types.InlineKeyboardButton('Перейдите по ссылке для решения задач', url='https://leetcode.com/studyplan/top-interview-150/')
            markup.row(btn)
            bot.reply_to(message, 'Уфф... Хороший будет апгрейд! Успехов чемп🫡', reply_markup=markup)

        elif message.text == '👽 стикер 👽':
            stick = open('./static/stick.png', 'rb')
            bot.send_sticker(message.chat.id, stick)

        elif message.text == '⬅️ назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🔎 roadmap 🔍')
            item2 = types.KeyboardButton('📩 новости мира IT 📩')
            item3 = types.KeyboardButton('👾 тесты  и стикер 👾')
            item4 = types.KeyboardButton('🎯 вопрос о сотрудничестве 🎯')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '⬅️ назад', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, f'Упс, {message.from_user.first_name}, начни с команды /start')



# запуск пока значение равно True
bot.polling(none_stop=True)