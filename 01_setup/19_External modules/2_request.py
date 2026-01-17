import requests

r = requests.get('https://api.github.com/events') #request package are used to get some data from the url and save that data from the text file
#print(r.text)

with open("C:/python prog/01_setup/19_External modules/Ali.txt", "w", encoding="utf-8") as f:
    f.write(r.text)
