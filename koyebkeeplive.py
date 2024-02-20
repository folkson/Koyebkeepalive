import requests

url = "https://555-vms.koyeb.app/"

# 定义浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    print("请求成功！")
    print("响应内容：", response.text)
else:
    print("请求失败，状态码：", response.status_code)
