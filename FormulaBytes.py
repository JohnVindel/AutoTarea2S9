#Tarea 2 - Formula de Bytes
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['gigabytes-megabytes', 'gb-mb', 'megabyte', 'mb'])
def info(mensaje):
    bot.reply_to(mensaje, "mb = 1gb * 1024mb")
    print("Gigabytes a Megabytes")

@bot.message_handler(commands=['terabytes-gigabytes', 'tb-gb', 'gigabyte', 'gb'])
def info(mensaje):
    bot.reply_to(mensaje, "gb = 1tb * 1024gb")
    print("Terabytes a Gigabytes")

@bot.message_handler(commands=['megabytes-kilobytes', 'mb-kb', 'kilobyte', 'kb'])
def info(mensaje):
    bot.reply_to(mensaje, "kb = 1mb * 1024kb")
    print("Megabytes a Kilobytes")

@bot.message_handler(commands=['bytes-bits', 'b-bit', 'bit'])
def info(mensaje):
    bot.reply_to(mensaje, "bit = 1b * 8bit")
    print("Bytes a Bits")

bot.polling()