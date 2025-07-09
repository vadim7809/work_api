import requests



valcode = input("Введіть валюту: ")
date = input("Введіть дату :")

response = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&{date}=20250302&json")

print(response.status_code)
results = response.json()
print(results)

rate = results[0]["rate"]

price = 100 / rate

print(results[0])
print(price)
