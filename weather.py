import requests

appId = 'd3238c571a3a6b086dd349e7ec157fd9'
 
def get_weater(city:str):
    
    lat,lon = get_geo(city)
    
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=es&appid={appId}')
    
    if r.status_code == 200:
        
        info = r.json()
        print(f"Temperature : {info['main']['temp']}")
        print(f"Description : {info['weather'][0]['description']}")
        print(f"Humidity : {info['main']['humidity']}") 
        
        
    
def get_geo(city:str):
    r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={appId}')
    
    if r.status_code == 200:
        info = r.json()
        
        return ([info[0]['lat'],info[0]['lon']])