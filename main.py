from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = "data/" + str(now.strftime("%d-%m-%Y-%H")) + ".txt"

url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=ComfyIron"

print(not os.path.isfile(dt_string))

result = requests.get(url)
with open(dt_string, "x") as f:
    f.write(result.text)
