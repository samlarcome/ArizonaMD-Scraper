def find_residency(soup):
  tab = soup.find("table",{"id":"ContentPlaceHolder1_dtgEducation"}).find_all('tr')
  residencies = set()
  for tr in tab:
    tds = tr.find_all('td')
    foo = False
    curr = []
    for td in tds:
      # print(type(td.text)) -> string
      if foo:
        curr.append((td.text).strip())
      if td.text == "Residency:":
        foo = True
        curr.append((td.text.strip()))
  
    if len(curr) > 0:
      residencies.append(curr)

  return residencies



def board_actions(soup):
  try:
    boardlink = soup.find("a",{"id":"ContentPlaceHolder1_dtgBoard_btnLink_0"})["href"]

  except:
    boardlink = "None"

  return boardlink
