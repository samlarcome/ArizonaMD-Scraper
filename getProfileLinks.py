from unicodedata import name
import requests
from bs4 import BeautifulSoup
import json
from globals import headers as userAgent
from globals import specialtyPostValues

def getURLSTest(url, specialty):
    # header 

    s = requests.session()

    soup = BeautifulSoup(s.get(url, headers=userAgent).content, "html.parser")

    # dictionary to hold data needed for POST request
    data = {}

    for inputs in soup.select("input"):
        data[inputs.get("name")] = inputs.get("value", "")

    data["ctl00$ContentPlaceHolder1$Name"] = "rbName1"
    data["ctl00$ContentPlaceHolder1$License"] = "rbLicense1"
    data["ctl00$ContentPlaceHolder1$Specialty"] = "rbSpecialty1"
    data["ctl00$ContentPlaceHolder1$ddlSpecialty"] = specialtyPostValues[f"{specialty}SpecialtyCode"]
    data["ctl00$ContentPlaceHolder1$ddlCounty"] = "15910" # 15910
    data["__EVENTTARGET"] = "ctl00$ContentPlaceHolder1$btnSpecial"
    data["__EVENTARGUMENT"] = ""

    # grabs html returned from POST request
    html = s.post(url, data=data, headers=userAgent).content
    soup = BeautifulSoup(html, "html.parser")

    # data to dump to a JSON file
    jsondump = {}

    for row in soup.select("tr:has(a)"):
        name = row.select("td")[-1].text
        link = row.a["href"]

        # populate the object to dump to JSON
        jsondump[name] = link
        # print("{:<35} {}".format(name, link))

    # dump data into json file
    with open(f'./links/{specialty}ProviderLinks.json', 'w', encoding='utf-8') as f:
        json.dump(jsondump, f, ensure_ascii=False, indent=4)

    return jsondump, len(jsondump)

if __name__ == "__main__":
    getURLSTest(url = "https://azbomprod.azmd.gov/GLSuiteWeb/Clients/AZBOM/public/WebVerificationSearch.aspx?q=azmd&t=20220622082816")
