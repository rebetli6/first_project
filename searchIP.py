from json import load

file= open("MOCK_DATA.json", encoding="utf-8")
content= load(file)
mini = 255
for item in content:
    ip = item["ip_address"]
    prefix = int(ip.split(".")[0])
    if prefix < mini:
        mini=prefix
print(mini)



