from globals import arizonaMDLookupURL, headers
from getProfileLinks import getURLSTest
from scrapeFunctions import find_name, find_residency, find_board_actions
from bs4 import BeautifulSoup
import requests
import json

### ARIZONA - Can I go back and make which data scraped (functions called) more modular

# 1: Find what specialty
#  - Anesthesiology, Family Medicine, Hospitalist, Psychiatry, Radiology, Surgery, Surgical Oncology
options = {1: "Anesthesiology", 2:"Family Medicine", 3:"Psychiatry", 4:"Radiology", 5:"Surgery", 6:"Surgical Oncology"}  
print("Choose speciality in AZ: \n1 - Anesthesiology\n2 - Family Medicine\n3 - Psychiatry\n4 - Radiology\n5 - Surgery\n6 - Surgical Oncology")

userInput = int(input())

while(userInput < 1 or userInput > 6):
    print("Please enter a valid choice")
    userInput = int(input())

specialty = options[userInput]
print(f"You chose {specialty}")
# 2: Make post request to get the table full of provider profiles

# dictionary with the names and links to provider profiles
# calls function to retreive links to all profiles of that specialty
providerLinks, numProviders = getURLSTest(arizonaMDLookupURL, specialty)

print(f"There are {numProviders} providers")


# 3: Iterate over profiles - scraping the necessary data
    # Name, Board Data, Residencies
providerResidencies = []
for key in providerLinks:
    link = providerLinks[key]

    # send GET request to provider profile link
    # returns request.Resonse() object
    res = requests.get(link, headers=headers)
    if (res.status_code != 200):
        print("Did not make successful GET request")
        print("Status code: {}, Reason: {}".format(res.status_code, res.reason))
        break    

    # get content of response
    webpage = res.content

    soup = BeautifulSoup(webpage, "html.parser")

    # Object to store data for each provider
    currentProviderData = {}

    # Find the name of the provider (both ways)
    currentProviderData["Lastname_Firstname"] = key
    currentProviderData["Firstname_Lastname"] = find_name(soup)

    # Find if there are any board actions against the provider
    currentProviderData["Board Actions"] = find_board_actions(soup)

    # Find the residencies of the provider
    residencies = find_residency(soup)
    # Add each residency as a separate in the object
    count = 1
    for res in residencies:
        keyname = f"Residency {count}"
        currentProviderData[keyname] = res
        count += 1
    
    providerResidencies.append(currentProviderData)
    

# 4: Dump the data into a json file
with open(f'./data/{specialty}ProviderResidencies.json', 'w', encoding='utf-8') as f:
    json.dump(providerResidencies, f, ensure_ascii=False, indent=4)
