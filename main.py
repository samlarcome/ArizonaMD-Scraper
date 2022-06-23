from getURLS import getURLS
from globals import arizonaMDUrl, headers
from bs4 import BeautifulSoup
import requests
from scrapeFxn import find_residency

# Retrieves links to provider profiles
# Dumps into 'providerLinks.json'
# Returns the dictionary that is also dumped into json
providerLinks = getURLS(arizonaMDUrl)


providerData = {}

# iterate over providers/links
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
    # print(webpage)
    soup = BeautifulSoup(webpage, "html.parser")

    print(find_residency(soup))
    break
