import amino
import telebot
import time

Email = "danial7987@gmail.com"
Password = "o123o123"

client = amino.Client()
link = client.get_from_code("http://aminoapps.com/p/evxnta")
comId = link.path[1:link.path.index("/")]
chatId = link.objectId
client.login(Email, Password)
sub= amino.SubClient(comId=comId, profile=client.profile)

token = "5218688832:AAFEDBG9Udpd_XSiZ470dSBQlp50L00FCjg"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,"تم الأرسال بنجاح")
	sub.send_message(chatId=chatId, message='Test by telebot')
	
print("bot online")	
bot.polling(True)
	
