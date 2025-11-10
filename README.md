Reddit sentiment analyzer, based on online resources originally built for the Twitter API, which are now outdated. I targeted Reddit instead, which still has a free and accessible API.

The code fetches Reddit posts related to a given query and performs basic sentiment analysis on the post titles using TextBlob. It connects to Reddit via the praw API, searches the 50 most relevant posts in all subreddits, and computes:

Polarity (how positive or negative the text is)

Subjectivity (how subjective or opinionated the text is)

A sentiment label: "positif", "négatif", or "neutre" (positive, negative, neutral)

It then calculates the average polarity of all posts, prints it, and saves all data in a CSV file (reddit_sentiment.csv) including the post title, score, subreddit, polarity, subjectivity, sentiment, and URL.

Example usage in the code: queryForSentiment("Pizza Hut")
