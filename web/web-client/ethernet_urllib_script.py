import urllib.request as ur

url = 'https://www.multitran.ru/c/m.exe?CL=1&s=%FD%F0%F3%E4%E8%F2&l1=1' #'http:/www.iheartquotes.com/api/v1/random'
conn = ur.urlopen(url)
data = conn.read()
print(conn.status)
print(conn.getheader('Content-Type'))
for key, value in conn.getheaders():
    print(key, value)
print(data)