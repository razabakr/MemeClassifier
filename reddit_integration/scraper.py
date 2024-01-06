import tweepy
import requests

# Twitter API credentials
consumer_key = 'YCO7EEpOaYTS3B4CVpdCbwhT8'
consumer_secret = 'YOzjzHxNSn32dDBjKLXpgvizKfJMIPwKOS5C1rC8psos4L3CK5'
access_token = '951957010999734274-NspDDYifS9c1EtpA1TrPMBzwCxV39fs'
access_token_secret = 'E4rdkfdBxAjwH9yuK80JTlbgaxW3YMBFFC6negV2bP364'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch tweets from your timeline
tweets = api.home_timeline(count=1, tweet_mode='extended')  # Adjust count as needed

# Extract image URLs
image_urls = []
i = 0
for tweet in tweets:
    print(i)
    media = tweet.entities.get('media', [])
    # if len(media) > 0:
    #     image_urls.append(media[0]['media_url'])
    i += 1

# Download images
for i, url in enumerate(image_urls):
    img_data = requests.get(url).content
    with open(f'image_{i}.jpg', 'wb') as handler:
        handler.write(img_data)

# Now, you can preprocess these images and feed them into your model
