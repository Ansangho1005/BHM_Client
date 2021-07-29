
from BHM_config_json import *
from func_autogui import *
from func_main import *
import constant 


if __name__ == "__main__":
    json_data = readjson(isfileindoc())
    
    temp = startApp('1613812926')
    print(temp[1])
