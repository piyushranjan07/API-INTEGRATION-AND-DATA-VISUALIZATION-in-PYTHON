# Import necessary libraries
import requests                     # To make HTTP requests to the weather API
import matplotlib.pyplot as plt     # plotting of temperature data

API_KEY = 'API Key'   # Define API key

CITY = 'Pupri'        # enter place for fencing weather data

# Construct the API URL
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Send the GET request to OpenWeatherMap API
response = requests.get(URL)

# Parse the JSON response
data = response.json()

# Print the response for debugging
print(data)  

# Initialize empty lists to store temperature and timestamp data
temps = []
times = []

# Check if the 'list' key exists in the response
if 'list' in data:

    for entry in data['list']:
        temps.append(entry['main']['temp'])
        times.append(entry['dt_txt'])
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(times[:10], temps[:10], marker='o')
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (Celsius)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    # If the API response doesn't contain the expected data
    print("Error in API response:", data.get('message', 'Unknown error'))
