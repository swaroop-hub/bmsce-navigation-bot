import telepot

token = "830888701:AAFXoS8n6Jm9iDGztW4CWJMG1o54qpvrCZ8"

TelegramBot = telepot.Bot(token)


print (TelegramBot.getMe())
print(TelegramBot.getUpdates())