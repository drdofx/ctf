import re
import requests

message = "(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)"                                                                                                                                                                                                       
cleaned_message = re.sub("[)_]", "", message)                                                                                                                                                                                                   

arr = cleaned_message.split("(")                                                                                                                                                                                                                
arr.pop(0)

text = ""

for i in range(len(arr)):
    place = arr[i].split(",")
    r = requests.get(f"https://us1.locationiq.com/v1/reverse.php?key=pk.f83ed45d5a33d547929c06e7248c0f80&lat={place[0]}&lon={place[1]}&format=json")    
    addr = r.json()["address"]
    if ("city" in addr):
        text += f"{addr['city'][0]}"
    elif ("province" in addr):
        text += f"{addr['province'][0]}"
    elif ("county" in addr):
        text += f"{addr['county'][0]}"

print(text)