import configparser
from telethon import TelegramClient, events, sync
from datetime import datetime
import threading
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
from telethon import TelegramClient

from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.functions.channels import GetParticipantsRequest

from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch

def is_member(name,channel_username,user_id):
    for user in client.iter_participants(channel_username, search=name):
        if user.id == user_id:
            return True
    return False
            
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

channel_users = []

with TelegramClient('ali_fatahi', api_id, api_hash) as client:
    print("Connected")      
    f = open("blacklist.txt", "r")
    blacklist = f.read()  
    f = open("message.txt", "r",encoding = "utf-8")
    message = f.read() 
    targets_count = 0
    i = 0
    for dialog in client.iter_dialogs():       
        try:
            print(str(i)+"th dialog")
            i+=1
            if str(dialog.entity.id) not in blacklist:
                if not is_member(dialog.name,'fallen_games',int(dialog.entity.id)):
                    if not str(type(dialog.entity)) == "<class 'telethon.tl.types.Channel'>":
                        if dialog.entity.bot == False:
                                targets_count += 1
                                print("targets:"+ str(targets_count))
                                # client.send_message(entity=dialog.entity,message=message)
                                f = open("blacklist.txt", "a")
                                f.write(str(dialog.entity.id)+ "\n")
                                f.close()
                    else:
                        f = open("blacklist.txt", "a")
                        f.write(str(dialog.entity.id)+ "\n")
                        f.close()            
                else:
                    f = open("blacklist.txt", "a")
                    f.write(str(dialog.entity.id)+ "\n")
                    f.close()

        except:
            continue    
          
            
