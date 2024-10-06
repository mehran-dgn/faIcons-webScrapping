import requests
import json
from bs4 import BeautifulSoup

url = "https://fontawesome.com/v4/icons/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content , 'html.parser')
    icons_list_rows = soup.find_all(class_="fontawesome-icon-list")
    icons_list = []
    for row in icons_list_rows:
        icons = row.find_all('i')
        for icon in icons:
            icon_class_str = ""
            for i in icon['class']:
                icon_class_str += f"{i} "
            icons_list.append(icon_class_str.rstrip())
    # print(icons_list)
    filename = "icons.json"
    with open(filename,"w") as json_file:
        json.dump(icons_list , json_file)
        

else:
    print("Something went wrong , status code:",response.status_code)

