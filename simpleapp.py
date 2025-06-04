# Import the requests library to make HTTP calls to the weather API
import requests

# Replace 'x' with your actual API key from OpenWeatherMap
API_KEY = 'x'

# Define a function to get weather data for a given city
# It takes the city name and units (imperial or metric) as input
def get_weather(city, units="imperial"):
    try:
        # Make an API call to OpenWeatherMap with the given city and units
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={API_KEY}"
        )

        # Convert the response to JSON so we can access it like a dictionary
        data = response.json()

        # Check if the API returned a "city not found" error (404)
        if response.status_code == 404 or data.get('cod') == '404':
            return None, "City not found."
        
        # Handle any other unexpected errors (e.g., wrong API key, server error)
        elif response.status_code != 200:
            return None, f"Error: {data.get('message', 'Unknown error')}"
        
        # If everything is okay, return the data and no error message
        return data, None

    # Handle network errors such as no internet connection
    except requests.exceptions.RequestException:
        return None, "Network error. Please check your internet connection."

# Define a helper function to return an emoji based on the weather condition
def weather_emoji(condition):
    # Map known weather conditions to emojis
    emojis = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️"
    }
    # Return the matching emoji or an empty string if condition is unknown
    return emojis.get(condition, "")

# Ask the user which temperature unit they prefer (Celsius or Fahrenheit)
unit_choice = input("Choose temperature unit - (C)elsius or (F)ahrenheit: ").strip().lower()

# Set units to "metric" for Celsius, else default to "imperial" for Fahrenheit
units = "metric" if unit_choice == "c" else "imperial"

# Choose the correct unit symbol for display
temp_unit = "°C" if units == "metric" else "°F"

# Tell the user how to use the app
print("\nType a city name to get the weather or 'q' to quit.\n")

# Start an infinite loop to allow multiple city checks
while True:
    # Prompt the user to enter a city
    city = input("Enter city: ").strip()

    # If the user enters 'q', exit the loop and end the program
    if city.lower() == 'q':
        print("Goodbye! 👋")
        break

    # Call the get_weather function with the user's input
    data, error = get_weather(city, units)

    # If there was an error (e.g., city not found, network error), show it
    if error:
        print(f"❌ {error}\n")

    # If data was successfully fetched, format and display it
    else:
        # Get the main weather condition (e.g., Clear, Rain)
        weather = data['weather'][0]['main']

        # Get the appropriate emoji for the weather
        emoji = weather_emoji(weather)

        # Round the temperature value to the nearest integer
        temp = round(data['main']['temp'])

        # Print a formatted weather summary
        print(f"✅ {city.title()} | {weather} {emoji} | {temp}{temp_unit}")

        # Print a divider line for visual clarity
        print("-" * 40)
