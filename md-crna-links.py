from unicodedata import name
import requests
from bs4 import BeautifulSoup
import json

def getURLS():
    # header 

    s = requests.session()

    url = "http://lookup.mbon.org/verification/Search.aspx"
    userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    soup = BeautifulSoup(s.get(url, headers=userAgent).content, "html.parser")

    # # dictionary to hold data needed for POST request
    data = {}

    for inputs in soup.select("input"):
        data[inputs.get("name")] = inputs.get("value", "")

    data["t_web_lookup__license_type_name"] = "CRNA"
    data["t_web_lookup__profession_name"] = "Nursing"
    data["sch_button"] = "Search"
    
    data["__EVENTTARGET"] = ""
    data["__EVENTARGUMENT"] = ""
    data["__LASTFOCUS"] = ""

    # makes INITIAL POST request
    html = s.post(url, data=data, headers=userAgent).content
    
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", {"id": "datagrid_results"})





    # # data to dump to a JSON file
    jsondump = {}
    start = "http://lookup.mbon.org/verification/"

    for row in table.select("tr:has(a)"):
        name = row.a.text
        if (name=="License #" or name == "2"):
            continue
        link = start + row.a["href"]
        # print(name)

    #     # populate the object to dump to JSON
        jsondump[name] = link

    # # dump data into json file
    # with open('./data/MD-CRNA-Links.json', 'w', encoding='utf-8') as f:
    #     json.dump(jsondump, f, ensure_ascii=False, indent=4)

    # return jsondump




    next = table.find_all('tr')[-1].find('a').text
    while next is not None:
        pass

getURLS()
