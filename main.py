import requests
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com/"
count = 0

def scrap(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temp"]
    return value


def write(date, temperature):
    with open("data.txt", "a") as file:
        file.write(f"{date},{temperature}" + "\n")


if __name__ == "__main__":
    while count < 10:
        scrapped = scrap(URL)
        temperature = extract(scrapped)
        now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        write(now, temperature)
        count = count + 1