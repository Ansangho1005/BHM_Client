import os, os.path, datetime, json, socket

from func_main import *
from http_server import *

JSONPATH = os.path.expanduser('~\Documents\BHM\BHM_config.json')

def readjson(jsonpath):
    if jsonpath:
            with open(JSONPATH, "r") as fp:
                loaded = json.load(fp)
                return loaded
    else:
        data_set = dict()

        basicInfo = dict()
        basicInfo['PK_CLINET'] = issueclientPK()
        basicInfo["CHAT_ID"] = ""
        data_set["BASIC_INFO"] = basicInfo

        hostInfo = dict()
        hostInfo["INSTALL_DATE"] = str(datetime.datetime.now())
        hostInfo["CLIENT_HOST_NAME"] = str(socket.gethostname())
        hostInfo["CLIENT_IP_EX"] = str(socket.gethostbyname(socket.getfqdn()))
        data_set["HOST_INFO"] = hostInfo

        record = dict()
        record["CNT_SUCCESS_QUEUE"] = ""
        record["CNT_SUCCESS_GAME"] = ""
        data_set["RECORD"] = record
        
        print(JSONPATH)
        with open(JSONPATH, 'w', encoding='utf-8') as w_fp:
            json.dump(data_set, w_fp, indent="\t")

def modifyJson(category, key, value):
    with open(JSONPATH, 'r') as f:
        json_data = json.load(f)
    json_data[category][key] = value
    with open(JSONPATH, 'w', encoding='utf-8') as w_fp:
        json.dump(json_data, w_fp, indent="\t")