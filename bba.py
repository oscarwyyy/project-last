import praw
import pandas as pd

# Setup Reddit API client
reddit = praw.Reddit(client_id='your_client_id', 
                     client_secret='your_client_secret', 
                     user_agent='your_user_agent')

# Fetch posts from a specific subreddit
subreddit = reddit.subreddit('python')
posts = []

for post in subreddit.hot(limit=1000):  # Adjust limit as needed
    posts.append({
        'Title': post.title,
        'Score': post.score,
        'URL': post.url,
        'Date Created': post.created_utc,
        'Comments': post.num_comments
    })

# Convert to DataFrame
df = pd.DataFrame(posts)

# Export to CSV
df.to_csv('reddit_posts.csv', index=False)
print(df.head())
