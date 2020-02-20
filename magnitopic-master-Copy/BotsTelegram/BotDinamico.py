# -*- coding: UTF8 -*-
import requests
import datetime
import random as rd


class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_photo(self, chat_id,url):
        #params = {'chat_id': chat_id, 'photo': photo, 'parse_mode': 'HTML'}
        method = 'sendPhoto'
        resp = requests.post(self.api_url + method +'?chat_id=' + str(chat_id) + '&photo=' + url)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '830888701:AAFXoS8n6Jm9iDGztW4CWJMG1o54qpvrCZ8' #Token of your bot
walle_bot = BotHandler(token) #Your bot's name

sticker = ['👍','😁','😀','😂','👍🏼','❤️','👌','😎','😊']
re_stickers = ['👍','😊','😎']

def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=walle_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == 'hi' or first_chat_text == 'Hi' or first_chat_text == 'hey' or first_chat_text == 'Hey':
                    walle_bot.send_message(first_chat_id, 'Hello ' + first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text == '/start':
                    walle_bot.send_message(first_chat_id,'Hi ' + first_chat_name + 'Welcome to BMSCE')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'how are you' or first_chat_text == 'How are you':
                    walle_bot.send_message(first_chat_id, 'Im fine\nhow about you ' + first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text == 'what is your name':
                    walle_bot.send_message(first_chat_id, 'My name is Wall-E\nI guide people to their Destination ' + first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text == 'what can you do for me' or first_chat_text == 'What can you do for me':
                    walle_bot.send_message(first_chat_id, 'I\'m your personal navigator\nWhere do you want go\n(please enter your start point and destination\nEg:Main entrance toAcademic block\nor nearest metro station) ' )
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Nearest metro station' or first_chat_text == 'nearest metro station' or first_chat_text == 'metro station near me' or first_chat_text == 'Metro station near me':
                    walle_bot.send_message(first_chat_id, 'National College Metro Station(1.7 km)\nClick on the link to get directions\nhttps://goo.gl/maps/5d3FrkfiUb4JweaD8 ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Bus stop near me' or first_chat_text == 'bus stop near me' or first_chat_text == 'nearest bus stop' or first_chat_text == 'Nearest bus stop':
                    walle_bot.send_message(first_chat_id, 'Ganesh bhavan Bus Stop(towards Majestic)(600 m)\nhttps://goo.gl/maps/SGf9JJ1tGePHndNE8')
                    walle_bot.send_message(first_chat_id,'N R Colony Bus Stop(Towards Uttarhalli and Chikkallasndra)(700 m)\nhttps://goo.gl/maps/ktWG1RBPdteidaTg8')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Eatouts' or first_chat_text == 'Canteen' or first_chat_text == 'canteen' or first_chat_text == 'eatouts':
                    walle_bot.send_message(first_chat_id, 'There are 4 ' + first_chat_text + ' in campus:\n1.Vidyarthi Khana\n2.Back Canteen\n3.Kushka Canteen\n4.Kappi Kuttera\nChoose one')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to academic block' or first_chat_text == 'main entrance to academic block' or first_chat_text == 'front gate to academic block':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 50m\nYou will find your Destination on the left')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to indoor stadium' or first_chat_text == 'main entrance to indoor stadium' or first_chat_text == 'Vidyarthi khana' or first_chat_text == 'vidyarthi khana' or first_chat_text == 'Placement cell' or first_chat_text == 'placement cell':
                    walle_bot.send_message(first_chat_id, 'Walk straight\nTake the first left and continue for 150m\nYou will find your Destination on the Right')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Kappi kuttera' or first_chat_text == 'kappi kuttera':
                    walle_bot.send_message(first_chat_id, 'Walk straight \nAfter the first building block\nTake left\nYou will find your Destination on the Left after 10 m')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Kushka canteen' or first_chat_text == 'kushka canteen':
                    walle_bot.send_message(first_chat_id, 'Walk straight \nTake the first right\nContinue for 100 m\nYou will find your Destination at the end of the path')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to mechanical block' or first_chat_text == 'main entrance to mechanical block':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100 m\nYou will find your Destination on the Right')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to ISE dept' or first_chat_text == 'main entrance to ise dept':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 50m\nYou will find the Academic block\n5th floor in the Academic block is your Destination')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to CSE dept' or first_chat_text == 'main entrance to cse dept':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 50m\nYou will find the Academic block\n4th floor in the Academic block is your Destination')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to ECE dept' or first_chat_text == 'main entrance to ece dept':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 50m\nYou will find the Academic block\n3rd floor in the Academic block is your Destination')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to  Biotech dept' or first_chat_text == 'main entrance to biotech dept':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 50m\nYou will find the Academic block\n5th floor in the Academic block is your Destination')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to Telecom dept' or first_chat_text == 'main entrance to telecom dept':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 50m\nYou will find the Academic block\n5th floor in the Academic block is your Destination')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to pg block' or first_chat_text == 'main entrance to pg block':
                    walle_bot.send_message(first_chat_id, 'Walk straight\nThe second Building to your left is your Destination')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to allahabad bank' or first_chat_text == 'main entrance to allahabad bank' :
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue untill you reach a Gate\nWalk staright 50 m\nYou will find your Destination on the left')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to college mess' or first_chat_text == 'main entrance to college mess' or first_chat_text == 'Back canteen' or first_chat_text == 'back canteen':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue untill you reach a Gate\nWalk staright 50 m\nYou will find your Destination on the left')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to chemistry lab' or first_chat_text == 'main entrance to chemistry lab':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 500m\nYou will find your destination in the ground floor in the science block towards your right ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Main entrance to physics lab' or first_chat_text == 'main entrance to physics lab':
                    walle_bot.send_message(first_chat_id, 'Walk straight for 100m till Mechanical Block\nTake a left and continue for 500m\nYou will find your destination in the 2nd floor in the science block towards your right ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'bye' or first_chat_text == 'Bye' or first_chat_text == 'take care' or first_chat_text == 'Take care' or first_chat_text == 'see ya' or first_chat_text == 'See ya':
                    walle_bot.send_message(first_chat_id, 'Bye')
                    walle_bot.send_message(first_chat_id, 'It was nice talking to you\nSee you again later')
                    new_offset = first_update_id + 1
                elif first_chat_text in sticker:
                    walle_bot.send_message(first_chat_id,'👍')
                    new_offset = first_update_id + 1
                else:
                    walle_bot.send_message(first_chat_id, 'Sorry I cant understand '+ first_chat_name + '\nTry typing \"what can you do for me\"')
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
