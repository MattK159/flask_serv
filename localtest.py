import requests

diabvals = {'model': 1, 'np': 6, "pgc": 148, "dpb": 72, "tst": 35, "si": 0, "bmi": 33.6, "dpf": 0.627, "age": 50}
canvals = {'model': 2, 'age': 48, "bmi": 23.5, "gluc": 70, "inc": 2.707, "HOMA": 0.467408667, "lep": 8.8071, "adi": 9.7024, "res": 7.99585, "mcp": 417.114}
heartvals = {'model': 3, 'age': 48, "bmi": 23.5, "gluc": 70, "inc": 2.707, "HOMA": 0.467408667, "lep": 8.8071, "adi": 9.7024, "res": 7.99585, "mcp": 11.114, "aa": 16.114, "ab": 10.114, "ac": 17.114, "ac": 12}

print(len(heartvals))

result = requests.get("http://0.0.0.0:5000", params = diabvals)
print(result.json())

result = requests.get("http://0.0.0.0:5000", params = canvals)
print(result.json())

result = requests.get("http://0.0.0.0:5000", params = heartvals)
print(result.json())