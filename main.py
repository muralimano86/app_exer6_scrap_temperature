import requests
import selectorlib
import datetime

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
        file.write(f"{date}, {temperature}" + "\n")


if __name__ == "__main__":
    while count < 10:
        scrapped = scrap(URL)
        temperature = extract(scrapped)
        date_file = datetime.datetime.strftime(datetime.datetime.now(), "%y-%m-%d-%H-%M-%S")
        write(date_file, temperature)
        count = count + 1