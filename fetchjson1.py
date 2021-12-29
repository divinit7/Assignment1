import json

import pandas as pd
import requests

link = "https://s3.amazonaws.com/open-to-cors/assignment.json"

def jsonTohtml():
    f = requests.get(link)
    json_data = json.loads(f.text)
    data = pd.DataFrame.from_dict(json_data["products"], orient="index")
    data.sort_values(by=['popularity'], ascending=False)
    htmlDf = data.to_html()
    return htmlDf

html = jsonTohtml()

text_file = open("./templates/index.html", "w")
text_file.write(html)
text_file.close()
