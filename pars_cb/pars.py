import requests
from bs4 import BeautifulSoup

url = "https://cbr.ru/currency_base/daily/" 

headers = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

req = requests.get(url, headers=headers)
src = req.text
#print(src)

with open("index.html", "w") as file:
    file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_wal = soup.find_all(class_="data")

list_info = []
for i in all_wal:
    item_text = i.text
    list_info.append(item_text)
    
all_info = "".join(list_info)

nes_info = all_info.split("\n\n\n")
usd_info = []
for i in range(len(nes_info)):
    if "USD" in nes_info[i]:
        usd_list = nes_info[i]

value = usd_list.split("\n")
sum = int(input("Введите сумму в рублях: "))
convert = sum/float(value[4].replace(",", "."))
print(f"{convert:.2f}")