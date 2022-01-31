from config import TG_TOKEN
import telebot
import sqlite3
import arrow
import os
from web_scrapping import get_data
from read_data import read_data
from arima_prediction import predict
from plotting import plot


bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['help'])
def help(message):
	text_to_send = 'Creating plots and prediction for StockMarket'
	bot.send_message(message.from_user.id, str(text_to_send))


def manage_db(chat_id, msg_txt):
	con = sqlite3.connect('history.db')
	cur = con.cursor()
	now = arrow.now()
	cur.execute("INSERT INTO requests VALUES (?, ?, ?)", (now.format('DD-MM-YYYY HH:mm'), chat_id, msg_txt))
	con.commit()
	con.close()


@bot.message_handler(commands=['my_id'])
def get_my_id(message):
	if message.text == "history":
		con = sqlite3.connect('history.db')
		cur = con.cursor()
		for row in cur.execute('SELECT * FROM requests'):
			bot.send_message(message.from_user.id, str(row))


def check_downloads(name):
	folder = os.listdir('data')
	for i in folder:
		if i == str(name)+'.csv':
			return True
	return False


def return_visual_for_data(data_set_name):
	Date, Open, Close, Volume = read_data(data_set_name)
	number_of_predictions = 3
	open_predict = predict(Open, number_of_predictions)
	close_predict = predict(Close, number_of_predictions)
	volume_predict = predict(Volume, number_of_predictions)
	new_idnex = [x + len(Date) - 1 for x in range(0, number_of_predictions + 1)]
	plot(Date, Open, new_idnex, open_predict, 'open price')
	plot(Date, Close, new_idnex, close_predict, 'close price')
	plot(Date, Volume, new_idnex, volume_predict, 'volume')



@bot.message_handler(func=lambda message: True)
def msg_handler(message):
	manage_db(message.from_user.id, message.text)
	if check_downloads(message.text):
		return_visual_for_data(message.text)
	else:
		get_data(message.text)
		return_visual_for_data(message.text)

	photo = open('open price.png', 'rb')
	bot.send_photo(message.from_user.id, photo)
	photo = open('close price.png', 'rb')
	bot.send_photo(message.from_user.id, photo)
	photo = open('volume.png', 'rb')
	bot.send_photo(message.from_user.id, photo)


	# bot.send_message(message.from_user.id, str(message.from_user.id))
	# bot.reply_to(message, message.text)


bot.polling()
