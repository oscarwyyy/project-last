from google_play_scraper import app, reviews
import pandas as pd

apps = ['com.whatsapp', 'com.facebook.katana', 'com.instagram.android', 'com.snapchat.android']

app_data = []

for app_id in apps:
    result = app(app_id)
    app_reviews, _ = reviews(app_id, count=1000)  # Get 1000 reviews for the app

    # Now app_reviews is a list, and you can process it
    review_data = [{'User': review['userName'], 'Review': review['content'], 'Rating': review['score']} for review in app_reviews]

    app_data.append({
        'App Name': result['title'],
        'Rating': result['score'],
        'Reviews': result['ratings'],
        'Installs': result['installs'],
        'Price': result['price'],
        'Reviews Data': review_data  # Add reviews as well
    })

df = pd.DataFrame(app_data)

df.to_csv('playstore_apps_with_reviews.csv', index=False)
print(df.head())
