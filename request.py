import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Distance':10, 'Temperature (°C)':10, 'Humidity (%)':60,'Wind Speed (m/s)':3,
                            'Haversine':1000, 'Solar radiation (MJ/m2)':0, 'PLong (km)':0, 'DLong (km)':2,
                            'Pmonth':12,'Phour': 1, 'Dmonth':2, 'Dhour':2})

print(r.json())