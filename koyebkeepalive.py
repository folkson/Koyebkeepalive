import requests
import sys
import os
import time

def log(info: str):
    print(info)
    global desp
    desp = desp + info + "\n"

url = "https://gentle-felidae-vz.koyeb.app"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
TG_USER_ID = os.environ.get('TG_USER_ID')

def telegram():
    try:
        url = f"https://push.coco88.tk/bot{TG_BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': TG_USER_ID,
            'text': f"日志\n{desp}",
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=data)
        if response.status_code != 200:
            log('Telegram Bot 推送失败')
        else:
            log('Telegram Bot 推送成功')
    except Exception as e:
        log(f"Telegram推送时出错: {str(e)}")

desp = ""

for _ in range(5):
    response = requests.get(url, headers=headers)
    log(f"状态码：{response.status_code}")

    if TG_BOT_TOKEN and TG_USER_ID and len(desp) > 0:
        telegram()
    
    time.sleep(5)

sys.exit(0)
