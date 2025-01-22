import requests
import pandas as pd

# Function to fetch place details including reviews using Google Places API
def get_place_details(place_id, api_key):
    # Define the endpoint for the Places API
    endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
    
    # Prepare the parameters for the API request
    params = {
        'place_id': place_id,
        'key': api_key,
    }
    
    # Make the API request
    response = requests.get(endpoint, params=params)
    
    # Parse the response JSON
    place_data = response.json()

    # Debugging: Print the response to check what data is returned
    print(f"API Response for Place ID {place_id}: {place_data}")
    
    # Extract place name, rating, and reviews if available
    if place_data['status'] == 'OK':
        result = place_data['result']
        name = result.get('name', 'N/A')
        rating = result.get('rating', 'N/A')
        reviews = result.get('reviews', [])
        
        review_texts = [review['text'] for review in reviews]
        
        return {'Name': name, 'Rating': rating, 'Reviews': review_texts}
    else:
        return {'Name': 'N/A', 'Rating': 'N/A', 'Reviews': []}

# Example list of place IDs (ensure these are correct)
place_ids = [
    'ChIJeRpOeF6j3UYR1bQ9dD6f_gA',  # Example place ID for a location
    'ChIJVXealLUv2IcRZFW1eO5K3n4',  # Example place ID for a location
]

# Your Google Maps API key
api_key = 'YOUR_GOOGLE_MAPS_API_KEY'

# List to store all location details
location_data = []

# Loop through the place IDs and fetch details
for place_id in place_ids:
    place_details = get_place_details(place_id, api_key)
    location_data.append(place_details)

# Convert the location data to a pandas DataFrame
df = pd.DataFrame(location_data)

# Export the data to a CSV file
df.to_csv('google_maps_reviews.csv', index=False)

# Print the first few rows of the DataFrame
print(df.head())

{
  "result": {
    "name": "Eiffel Tower",
    "rating": 4.7,
    "reviews": [
      {
        "author_name": "John Doe",
        "author_url": "https://plus.google.com/123456789",
        "language": "en",
        "profile_photo_url": "https://lh3.googleusercontent.com/...",
        "text": "Amazing landmark!",
        "time": 1626174400
      },
      {
        "author_name": "Jane Doe",
        "author_url": "https://plus.google.com/987654321",
        "language": "en",
        "profile_photo_url": "https://lh3.googleusercontent.com/...",
        "text": "Wonderful experience, a must-see!",
        "time": 1626174500
      }
    ]
  },
  "status": "OK"
}
