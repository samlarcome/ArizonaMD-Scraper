def find_residency(soup):
  try:
    tab = soup.find("table",{"id":"ContentPlaceHolder1_dtgEducation"}).find_all('tr')
  except:
    print("No table")
    return ["Not Available"]
  # Surgical Oncology - ContentPlaceHolder1_dtgEducation
  # ANX - ContentPlaceHolder1_dtgEducation
  # Radiology - ContentPlaceHolder1_dtgEducation
  residencies = []
  for tr in tab:
    tds = tr.find_all('td')
    foo = False
    # curr = []
    curr = ""
    for td in tds:
      # print(type(td.text)) -> string
      if foo:
        text = (td.text).strip()
        cleaned = " ".join(text.split())
        # curr.append(cleaned)
        curr += cleaned
      if td.text == "Residency:":
        foo = True
        # curr.append((td.text.strip()))
  
    if len(curr) > 0:
      residencies.append(curr)

  return residencies

def find_board_actions(soup):
  try:
    boardlink = soup.find("a",{"id":"ContentPlaceHolder1_dtgBoard_btnLink_0"})["href"]

  except:
    boardlink = " "

  return boardlink

def find_name(soup):
  # name = soup.find('b')
  # return name.text
  b = soup.find("span", {"id": "ContentPlaceHolder1_dtgGeneral_lblLeftColumnEntName_0"}).find("b")
  return b.text
