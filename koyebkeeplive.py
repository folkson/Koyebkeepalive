import requests
import sys
import os

# 定义一些变量
desp = ""

def log(info: str):
    print(info)
    global desp
    desp = desp + info + "\n"


url = "https://555-vms.koyeb.app/"

# 定义浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    log("请求成功！")
    log("响应内容：" + str(response.text))
else:
    log("请求失败，状态码：" + str(response.status_code))


# 推送信息
TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
TG_USER_ID = os.environ.get('TG_USER_ID')

def telegram():
    try:
        url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': TG_USER_ID,
            'text': f"Freenom 域名续期日志\n{desp}",
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=data)
        if response.status_code != 200:
            log('Telegram Bot 推送失败')
        else:
            log('Telegram Bot 推送成功')
    except Exception as e:
        log(f"Telegram推送时出错: {str(e)}")

    # 消息推送
    if TG_BOT_TOKEN and TG_USER_ID and len(desp) > 0:
        telegram()
        sys.exit(0)