import requests

# Replace 'YOUR_API_KEY' with your actual Polygon API key
api_key = 'dxu01GwirVb1SSBJanLZqi0cP2scytdM'
symbol = 'AAPL'  # Replace with the stock symbol you're interested in

# Define the API endpoint
endpoint = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2022-01-01/2023-01-01?apiKey={api_key}'

# Make the API request
response = requests.get(endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    
    # Print the raw response for inspection
    print("Raw Response:")
    print(data)
    
    # If you want to extract and print specific information, you can do so here
    if 'results' in data:
        results = data['results']
        print("\nExtracted Information:")
        for result in results:
            print(f"Timestamp: {result['t']}, Open: {result['o']}, Close: {result['c']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
