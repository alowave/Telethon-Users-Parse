from telethon import TelegramClient, sync
import time
from telethon.tl.functions.messages import ImportChatInviteRequest

API_ID = 123456 # 'YOUR API ID   '
API_HASH = 'YOUR HASH'
SESSION = 'parse_session'

client = TelegramClient(session=SESSION, api_id=API_ID, api_hash=API_HASH, app_version='0.0.1')
client.start()
client.get_dialogs()

link = "CHAT LINK"

try:
    client(ImportChatInviteRequest(link))
except:
    pass

join = client.get_entity(link)

print('Telethon-Users-Parse\n   Created by @alowave')
title = join.title
runtime = int(time.time())

f = open('Users ' + title.replace('"', "'") + ' ' + time.ctime(runtime).replace(':', '.') + '.txt', 'a', encoding = 'utf-8')

users = client.get_participants(join.id, aggressive=True)
a = {}

f.write(str(runtime) + ' - ' + title)
f.write('\nПолучено ' + str(len(users)) + ' из ' + str(users.total) + ' пользователей.\n')

for user in users:
    if user.username == None:
        username = 'None'
    else:
        username = user.username
    a[user.id] = username

sort_users =  sorted(a)
for user in sort_users:
    user_str = str(user) + ' : ' + a[user]
    print(user_str)
    f.write('\n' + user_str)

print('\nПолучено ' + str(len(users)) + ' из ' + str(users.total) + ' пользователей')
f.close()
input('Press Enter to exit.')