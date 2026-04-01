import requests

# Correct API key format (inside quotes)
API_KEY = "f70ffe81489703f1b3dcefe5a2b2465c"

# Ask user for city name
city = input("Enter city name: ")

# Correct API request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Debug output
print("API Response:", data)

# Check response status
if response.status_code == 200:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\nWeather Details")
    print("-------------------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)

else:
    print("Error:", data["message"])