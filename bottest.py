import amino
import telebot
import time


client = amino.Client()
link = client.get_from_code("http://aminoapps.com/p/evxnta")
comId = link.path[1:link.path.index("/")]
chatId = link.objectId
client.login_sid("AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICJlZjMxZmQ3MC1hNzgyLTQ1ZGYtYjBkMS03ZmM3MGQyMTY2NjUiLCAiNSI6IDE2NDY4NjQxMzEsICI0IjogIjc5LjIzNS4xNzEuNjAiLCAiNiI6IDEwMH1eBQOh2nA8EmklmfMXIJ7jZSWOpw")
sub= amino.SubClient(comId=comId, profile=client.profile)

token = "5218688832:AAFEDBG9Udpd_XSiZ470dSBQlp50L00FCjg"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,"تم الأرسال بنجاح")
	sub.send_message(chatId=chatId, message='Test by telebot')
	
print("bot online")	
bot.polling(True)
	
