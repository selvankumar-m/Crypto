import requests

url = 'http://localhost:5000/predict_api' 
r = requests.post(url,json={'Name':0, 'High':1788, 'Low':1888, 'Open':2021,'Day':8, 'Month':5,'Year':2021 })

print(r.json())