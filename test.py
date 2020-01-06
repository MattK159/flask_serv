import requests

diabvals = {'model': 1, 'np': 6, "pgc": 148, "dpb": 72, "tst": 35, "si": 0, "bmi": 33.6, "dpf": 0.627, "age": 50}
canvals = {'model': 2, 'age': 48, "bmi": 23.5, "gluc": 70, "inc": 2.707, "HOMA": 0.467408667, "lep": 8.8071, "adi": 9.7024, "res": 7.99585, "mcp": 417.114}
heartvals = {'model': 3, 'age': 48, "bmi": 1, "gluc": 1, "inc": 145, "HOMA": 233, "lep": 1, "adi": 2, "res": 150, "mcp": 0, "aa": 2.3, "ab": 3, "ac": 0, "ad": 6}



result = requests.get("https://arcane-earth-43004.herokuapp.com/", params = diabvals)
print(result.json())

result = requests.get("https://arcane-earth-43004.herokuapp.com/", params = canvals)
print(result.json())

result = requests.get("https://arcane-earth-43004.herokuapp.com/", params = heartvals)
print(result.json())