# Weather Info Retriever

import requests
 
def get_weather(lat=34.05,lon=-118.24):
    # Store your OpenWeatherMap API key here
    api_key = "your_api_key_here"
    
    # Create the URL to request data for the specified latitude and longitude
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    
    # Send a GET request to the API
    response = requests.get(base_url)
    
    # Convert the response to JSON format
    data = response.json()
 
    if response.status_code == 200:
        # Extract and display relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
 
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description}")
    else:
        print("Latitude/Longitude not found.")

  get_weather()
