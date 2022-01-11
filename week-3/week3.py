import urllib.request as ur
import json
import re

url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
resp=ur.urlopen(url)
raw_data=resp.read().decode('utf-8')
data=json.loads(raw_data)
data_len=len(data["result"]["results"])


with open("data.csv", mode="w", encoding="utf-8") as file:
    #抓資料
    for i in range(0, data_len):
        site=data["result"]["results"][i]["stitle"]

        district_raw=data["result"]["results"][i]["address"]
        district=re.findall('\s(\w+區)',district_raw)[0]


        longitude=data["result"]["results"][i]["longitude"]
        latitude=data["result"]["results"][i]["latitude"]

        photo_raw=data["result"]["results"][i]["file"]
        photo="http"+photo_raw.split("http")[1]
        
        final_data=f"{site},{district},{longitude},{latitude},{photo}"        

        #寫入csv        
        file.write(final_data+"\n")