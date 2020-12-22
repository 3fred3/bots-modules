from flask import Flask, request
import os
import telebot

#inicial conditions (SERVER, TOKEN, BOT)
server = Flask(__name__)
TOKEN ='YMNZA8TlGA3ybaNIS0qtXaVeBpmimGqnVlbx9WMIbqsPpCKuwlC75mzo5Bhwcb9V'# obivisioly this is a token example, it isnt gonna work
bot = telebot.TeleBot(token=TOKEN)

#functions
def find(msg):
    for text in msg:
        if '@' in text:
            return text

#commands body
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello (beep-bop), write /help to know more about me.')

@bot.message_handler(commands=['help'])
def imhelping(message):
    bot.reply_to(message,'Available commands. \n /help \n /vaidarbom \n /new or news)')

@bot.message_handler(commands=['vaidarbom'])
def deboa(message):
    bot.reply_to(message, 'Vai sim, sem pressa')

@bot.message_handler(commands=['new','news'])
def news(message):
    bot.reply_to(message, 'https://news.google.com/')

#@bot.message_handler(commands=['x','y'])
#def function_name(message):
#    bot.reply_to(message, 'average_msg_')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def insta_answer(message):
    texts = message.text.split()
    a_text = find(texts)
    if a_text == '@':
        pass
    else:
        bot.reply_to(message, 'https://instagram.com/{}'.format(a_text[1:]))

#webhook
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_url_heroku/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
