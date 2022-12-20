import json
import requests

def scrapeBooli(nPages,Tofile):
  f = open(Tofile,"a")
  f.write("[")
  json_txt = ""
  for i in range(1,nPages+1):
    URL = f"https://www.booli.se/slutpriser/vaxjo/116208?page={i}"
    page = requests.get(URL)
    index_start = page.text.find('"result":[{"__typename":"SoldProperty"')+10
    index_end = page.text[index_start:].find("]}}") -1 + index_start
    json_txt += page.text[index_start:index_end]

    sucess = fail = 0
    for entry in json_txt.split('{"__typename":"SoldProperty",')[1:]:
      try:
        entry = "{" + entry[:len(entry)-1] 
        json_object = json.loads(entry)
        bauty_json = json.dumps(json_object, sort_keys=True, indent=2)
        f.write(bauty_json+",")
        sucess += 1
      except:
        fail += 1
 
  print(f"Data added to {Tofile} {sucess} completed {fail} failed")
  f.write("]")
  f.close()