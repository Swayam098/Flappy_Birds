import requests
from requests.exceptions import ConnectionError, Timeout
import time

# Set the URL for the COVID-19 API endpoint
COUNTRY = 'india'
url = f"https://api.covid19api.com/dayone/country/{COUNTRY}"

# Retry logic and exception handling
for attempt in range(3):  # Retry 3 times
    try:
        response = requests.get(url, timeout=10)  # Set timeout to avoid hanging
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        
        # Parse the JSON response and print useful information
        data = response.json()

        print(f"COVID-19 Data for {COUNTRY} (From Day One):")
        
        # Extract the last day's data
        latest_data = data[-1]
        confirmed_cases = latest_data['Confirmed']
        deaths = latest_data['Deaths']
        recovered = latest_data['Recovered']
        date = latest_data['Date']

        print(f"Date: {date}")
        print(f"Confirmed cases: {confirmed_cases}")
        print(f"Deaths: {deaths}")
        print(f"Recovered: {recovered}")
        
        # Print sample data for the last 5 days
        print("\nSample data points (last 5 days):")
        for day_data in data[-5:]:
            print(f"Date: {day_data['Date']} -> Cases: {day_data['Confirmed']}, Deaths: {day_data['Deaths']}, Recovered: {day_data['Recovered']}")

        break  # If the request is successful, break the loop

    except ConnectionError as e:
        print(f"Connection error: {e}")
        time.sleep(5)  # Wait 5 seconds before retrying

    except Timeout:
        print("The request timed out")
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
