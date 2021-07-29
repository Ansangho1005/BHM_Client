from constant import HTTP_API
import telegram
import pyautogui

'''
chat = telegram.Bot(token = HTTP_API)
updates = chat.getUpdates()
for u in updates:
    print(u.message['chat']['id'])
'''
print(pyautogui.getActiveWindowTitle())
'''
def sendTemplateMessage_telegram (id = "1613812926", Msg = "Empty"):
    bot = telegram.Bot(token = HTTP_API)
    bot.sendMessage(chat_id = id, text=Msg)
    '''