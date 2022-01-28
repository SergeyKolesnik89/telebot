#телебот
import telebot

#случайности для анекдота
import random
import sqlite3 as sql
import sqlite3

#блок событий


from bs4 import BeautifulSoup
import requests

#для погоды

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import pyowm 


#Дата и время
import datetime as dt
from PyQt5.QtCore import QTimer, QTime, Qt
import time
import datetime as dt
import sys
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types


token = "1094693261:AAERSOmcqWAp38SMxc6Wbou_S8wTQsuLu8s"
bot = telebot.TeleBot("1094693261:AAERSOmcqWAp38SMxc6Wbou_S8wTQsuLu8s")
APP_URL = f'https://telegaechobot.herokuapp.com//{TOKEN}'

owm = OWM('b71a7de29575570f5971685c60ef5628')
owm.config["language"] = "ru"

keyboard1 = types.InlineKeyboardMarkup()
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Анекдот', 'Погода')
keyboard1.row( 'В этот день', 'О разработчиках')
#keyboard1.row('Гороскоп', 'В этот день', 'О разработчиках')

now = dt.datetime.utcnow()
today_now = now + dt.timedelta(hours=6) # 
print('Сейчас ' , today_now.strftime('%D %B %Y  %H:%M'),' по  времени астаны')
time_1 = today_now.strftime('%D%B%Y  %H:%M')

print (now)


   




@bot.message_handler(content_types=['text'])
    
def jokes_text(message):
    
    if message.text.lower() == 'анекдот':
        con = sql.connect('anekdot.db')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS 'test' ('number' INT, 'name' STRING)")
    
            cur.execute("SELECT * FROM 'test' ORDER BY RANDOM() LIMIT 1")
                
            rows = cur.fetchmany()
                
            for row in rows:
                    
                    
                bot.send_message(message.chat.id,row[0])



          
        con.commit()
        cur.close()

    

#Блок приветствия
    elif message.text == 'Привет':
        bot.send_message(message.from_user.id, 'О, привет, меня зовут Белка_bot и у меня лапки ^^ ')

    elif message.text.lower() == 'о разработчиках':
        bot.send_message(message.from_user.id, 'Мы скромные *_*')

#Блок событий

    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Я сказала стартуем )))",  reply_markup=keyboard1)
    
    elif message.text == 'В этот день':
        URL = 'https://kakoysegodnyaprazdnik.ru/'
        HEADERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
        }
        response = requests.get(URL, headers = HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        items = soup.findAll('div', class_='main')
        comps = []

        for item in items:
            comps.append({
            'title' : item.find('span').get_text(strip = True)
                            
            })

        global comp
        for comp in comps:
            bot.send_message(message.chat.id,(f'{comp["title"]}  '))
            print (f'{comp["title"]}  ')
            



    


        
#Блок погоды
            
    elif message.text.lower() == 'погода':
        
        bot.send_message(message.chat.id,'Введите город . . . ')
       
        
        
           
           
    try:
        
        #place = 'Petropavlovsk'
        if message.text == "привет" or message.text == "Привет":
            pass
        else:
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)
            print ('1')
            
            
            print ('2')
            w = observation.weather
            print ('3')
            temp = w.temperature('celsius')["temp"]
            print ('4')            
           
             
            answer = (f'В городе {message.text} сейчас { w.detailed_status } '"\n")
            
            bot.send_message(message.chat.id, answer)
            print ('5')
            answer = (f'Температура сейчас в районе  {temp}  градусов Цельсия' "\n\n")
            bot.send_message(message.chat.id, answer)
            print ('6')
            if temp <10:
                answer = "На улице холодно, одевайся очень тепло"
                print ('7')
            elif temp <20:
                answer = "Сейчас прохладно, одевайся теплее"
                print ('8')
            elif temp > 20:
                answer = "Надевай что хочешь, там тепло"
                print ('9')
            bot.send_message(message.chat.id, answer)
            
            print ('10')
    except:
        #bot.send_message(message.chat.id, "Некорректно введен город")
        print ('ошибка блеать')

    #else:
        #pass

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e) 
      
        time.sleep(2)

bot.polling(none_stop=True, interval=0)

input() 
