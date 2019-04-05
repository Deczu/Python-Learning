import requests
import json
from time import sleep
from time import strftime
from datetime import datetime

response = requests.get("OWM Api_key");
weatherJson = response.content;
parsedJson = json.loads(weatherJson);

print(response);
print(response.status_code)
print("\n")
print(response.headers);
print("\n")
print(response.content);
print("\n")


print(parsedJson)
print("\n")
print(parsedJson['name']);
print(parsedJson['main']['temp']);
print(parsedJson['main']['pressure']);
print(parsedJson['main']['humidity']);
print(parsedJson['weather'][0]['main']);


#with weatherJson as data_file:
 #   data = json.load(data_file)

while True:
    response = requests.get("OWM Api_key");
    weatherJson = response.content;

    if json.loads(weatherJson) == parsedJson:
        print("nothing changed \n");
    else:
        parsedJson = json.loads(weatherJson);
        print(parsedJson['name']);
        print(parsedJson['main']['temp']);
        print(parsedJson['main']['pressure']);
        print(parsedJson['main']['humidity']);
        print(parsedJson['weather'][0]['main']);
        



    sleep(5)
