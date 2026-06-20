import requests
import json
from datetime import datetime

def get_weather(city):
    """
    Fetch weather information for a given city using Open-Meteo API (free, no API key required)
    """
    try:
        # Using Open-Meteo API - free weather data
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        
        # Get city coordinates
        response = requests.get(url)
        data = response.json()
        
        if not data.get('results'):
            print(f"❌ City '{city}' not found!")
            return
        
        city_data = data['results'][0]
        latitude = city_data['latitude']
        longitude = city_data['longitude']
        city_name = city_data['name']
        country = city_data.get('country', '')
        
        # Get weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
        
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        # Display current weather
        current = weather_data['current']
        daily = weather_data['daily']
        
        print("\n" + "="*50)
        print(f"🌍 WEATHER REPORT FOR: {city_name}, {country}")
        print("="*50)
        
        # Current weather
        print(f"\n📍 Current Weather ({current['time']}):")
        print(f"   🌡️  Temperature: {current['temperature_2m']}°C")
        print(f"   💧 Humidity: {current['relative_humidity_2m']}%")
        print(f"   💨 Wind Speed: {current['wind_speed_10m']} km/h")
        print(f"   ☁️  Weather: {get_weather_description(current['weather_code'])}")
        
        # Forecast for next 3 days
        print(f"\n📅 3-Day Forecast:")
        for i in range(min(3, len(daily['time']))):
            date = daily['time'][i]
            max_temp = daily['temperature_2m_max'][i]
            min_temp = daily['temperature_2m_min'][i]
            precipitation = daily['precipitation_sum'][i]
            weather_code = daily['weather_code'][i]
            
            print(f"\n   📌 {date}")
            print(f"      High: {max_temp}°C | Low: {min_temp}°C")
            print(f"      Condition: {get_weather_description(weather_code)}")
            print(f"      Precipitation: {precipitation} mm")
        
        print("\n" + "="*50 + "\n")
        
    except requests.exceptions.ConnectionError:
        print("❌ Connection error! Please check your internet connection.")
    except Exception as e:
        print(f"❌ Error fetching weather data: {str(e)}")

def get_weather_description(code):
    """
    Convert WMO weather code to human-readable description
    """
    weather_codes = {
        0: "☀️ Clear sky",
        1: "🌤️ Mainly clear",
        2: "⛅ Partly cloudy",
        3: "☁️ Overcast",
        45: "🌫️ Foggy",
        48: "🌫️ Depositing rime fog",
        51: "🌧️ Light drizzle",
        53: "🌧️ Moderate drizzle",
        55: "🌧️ Dense drizzle",
        61: "🌧️ Slight rain",
        63: "🌧️ Moderate rain",
        65: "🌧️ Heavy rain",
        71: "🌨️ Slight snow",
        73: "🌨️ Moderate snow",
        75: "🌨️ Heavy snow",
        77: "🌨️ Snow grains",
        80: "🌧️ Slight rain showers",
        81: "🌧️ Moderate rain showers",
        82: "🌧️ Violent rain showers",
        85: "🌨️ Slight snow showers",
        86: "🌨️ Heavy snow showers",
        95: "⛈️ Thunderstorm",
        96: "⛈️ Thunderstorm with slight hail",
        99: "⛈️ Thunderstorm with heavy hail",
    }
    return weather_codes.get(code, "Unknown")

def main():
    """
    Main function to run the weather check application
    """
    print("\n" + "="*50)
    print("🌤️  WEATHER CHECK APPLICATION")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Check weather for a city")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == '1':
            city = input("Enter city name: ").strip()
            if city:
                get_weather(city)
            else:
                print("❌ Please enter a valid city name!")
        elif choice == '2':
            print("\n👋 Thank you for using Weather Check! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
