from BHM_config_json import modifyJson, openjsonforWrite
import os.path as path
import string, random, os, json , requests, pyautogui, datetime

from http_server import *
from func_autogui import *

def issueclientPK():
    LENTH = 6
    string_pool = string.ascii_uppercase + string.digits
    result = ""
    now = datetime.datetime.now()
    for i in range(LENTH):
        result += random.choice(string_pool)
    if now.day < 10 :
        day = "0" + str(now.day)
    else :
        day = str(now.day)
    result = result + day + str(now.hour) + str(now.minute) + str(now.second)
    if isPKonly(result) == True : #하나 밖에 없어서 status_code = 200을 받은 상황
        #modifyJson('BASIC_INFO', "PK_CLINET", result)
        return result
    elif isPKonly(result) == False:
        issueclientPK()
    else:
        return "PK를 발급하지 못함"
    
def isfileindoc():
    jsonpath = path.expanduser('~\Documents\BHM\BHM_config.json')
    if os.path.isfile(jsonpath) == True:
        return True
    else:
        return False

BASE_URL_FOR_SENDMSG = "http://127.0.0.1:8000/restbhm/sendmsg/" #/<int:chat_id>/<int:msg_type>/<int:try_cnt>/

def startApp (chatid):
        wouldyoulikesomethingtodrink = input("큐 자동수락 프로그램을 시작하겠슴둥? (yes or no)")
        cnt_accept = 0
        if wouldyoulikesomethingtodrink == 'yes':
            while(True):
                found_res = findUntil('autogui_image/accept.png')
                try:
                    if found_res == 0:
                        url = BASE_URL_FOR_SENDMSG + str(chatid) +"/11/" + str(cnt_accept) +"/"#11이 게임 시작 타입
                        response = requests.get(url)
                        print(response.status_code + "게임 시작 타입")
                        break
                    elif found_res == 1:
                        continue
                    else:
                        pyautogui.click(found_res)
                        cnt_accept = cnt_accept + 1
                        url = BASE_URL_FOR_SENDMSG + str(chatid) +"/10/" + str(cnt_accept) + "/" #10은 수락했을 때 메세지 타입
                        response = requests.get(url)
                        print(response.status_code + "큐 수락 타입")
                        #sendTemplateMessage_telegram("1613812926", str(cnt_accept) + "트 : 수락 버튼을 눌렀습니다.")
                except:
                    print("약간의 에러")
        else:
            return 100, "사용자가 앱을 실행하지 않음"
        return 1, "앱이 잘 종료됨"
