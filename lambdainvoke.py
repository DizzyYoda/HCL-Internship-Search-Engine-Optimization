import requests
import json

def lamda_keyword_ext(text):
    url='https://sdpbynidn8.execute-api.ap-south-1.amazonaws.com/test/invoke?text='
    url=url+text

    response_API = requests.get(url)
    data = response_API.text
    parse_json = json.loads(data)

    return parse_json

output=lamda_keyword_ext("Varun Kumar is working in HCL Technolgies");

print(output['text']);






