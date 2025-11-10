import praw
from textblob import TextBlob
import csv

def queryForSentiment(query):
    reddit = praw.Reddit(
        client_id="YOUR_ID_HERE",
        client_secret="YOUR_SECRET_HERE",
        user_agent="sentiment-analyzer by u/csiAfterlife",
    )

    query = query.lower()
    posts = reddit.subreddit("all").search(query, limit=50)

    data = []
    total_polarity = 0

    for post in posts:
        text = post.title
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        if polarity > 0.1:
            sentiment_label = "positif"
        elif polarity < -0.1:
            sentiment_label = "négatif"
        else:
            sentiment_label = "neutre"
        
        data.append({
            "title": text,
            "score": post.score,
            "subreddit": post.subreddit.display_name,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": sentiment_label,
            "url": post.url
        })
        
        total_polarity += polarity

    average_polarity = total_polarity / len(data) if data else 0
    print(f"Polarité moyenne des posts sur '{query}': {average_polarity:.2f}")

    csv_file = "reddit_sentiment.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerow({
            "title": f"Polarité moyenne : {average_polarity:.2f}",
            "polarity": average_polarity,
            "sentiment": "positif" if average_polarity > 0 else "négatif" if average_polarity < 0 else "neutre",
        })
        
        for row in data:
            writer.writerow(row)

    print(f"CSV créé : {csv_file}")


queryForSentiment("Pizza Hut")