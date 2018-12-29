import requests

url = 'https://www.multitran.ru/c/m.exe?CL=1&s=%FD%F0%F3%E4%E8%F2&l1=1' #'http:/www.iheartquotes.com/api/v1/random'
resp = requests.get(url)
resp
print(resp.text)