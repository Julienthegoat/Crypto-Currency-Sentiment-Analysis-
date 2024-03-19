import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
from praw import Reddit
import datetime
import time

# Initialize CryptoBERT
model_name = "ElKulako/cryptobert"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
crypto_sentiment_pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=64, truncation=True, padding='max_length')

# Reddit API credentials and initialization
reddit = Reddit(client_id='J19cj9blE8Eho_CFG7dOjQ',
                client_secret='-4WQFAt8ClCfngBd430Gy4snx2udIg',
                user_agent='YOUR_USER_AGENT')

# Function to fetch posts
def fetch_reddit_posts(subreddit, keyword, limit=15):
    posts = []
    subreddit_obj = reddit.subreddit(subreddit)
    if keyword:  # If there's a keyword, search for it
        submissions = subreddit_obj.search(keyword, limit=limit)
    else:  # If not, fetch the most recent posts
        submissions = subreddit_obj.new(limit=limit)  # Use .hot(), .new(), or .top() as needed

    for submission in submissions:
        posts.append(submission.title + ". " + submission.selftext)
    return posts

# Function to analyze sentiment with CryptoBERT
def analyze_sentiment(posts):
    results = []
    for post in posts:
        output = crypto_sentiment_pipeline(post)
        results.extend(output)
    return pd.DataFrame(results)



st.sidebar.title("Cryptocurrency Sentiment Analysis 🕵️ ")
page = st.sidebar.selectbox("Choose a page", ["Search by Token 🔍✨", "Search by SubReddit 📂", "Global Trends 🌍💱"])



if page == 'Search by Token 🔍✨':
    st.title('Search by Crypto Asset 🚀 👨‍🚀')
    crypto = st.text_input("Enter the cryptocurrency💲(e.g., $BTC, $ETH, $ADA):", value="$BTC")
    if st.button("Analyze Sentiment 🕵️"):
        
        with st.spinner("🌐 Fetching Reddit posts and analyzing sentiment..."):
            posts = fetch_reddit_posts("CryptoCurrency", crypto, 15)

            bar= st.progress(33)
            time.sleep(1)
            
            
            if posts:
                sentiment_df = analyze_sentiment(posts)
                # Map model output to readable sentiments
                label_map = {'LABEL_0': 'Bullish', 'LABEL_1': 'Neutral', 'LABEL_2': 'Bearish'}
                sentiment_df['label'] = sentiment_df['label'].map(lambda x: label_map.get(x, x))
                
                # Calculate and display sentiment probabilities
                sentiment_probs = sentiment_df['label'].value_counts(normalize=True) * 100
                sentiment_colors = {'Bullish': 'green', 'Neutral': '#FAA300', 'Bearish': 'red'}

                st.write(sentiment_probs)


            # Use a horizontal bar plot
                fig, ax = plt.subplots(facecolor='#0B0E12')
                sentiment_probs.plot(kind='barh', color=[sentiment_colors[label] for label in sentiment_probs.index], ax=ax)

                # Set the properties of the axes
                ax.set_facecolor('#0B0E12')
                ax.tick_params(colors='white', which='both')
                ax.spines['bottom'].set_color('black')
                ax.spines['left'].set_color('black')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                bar.progress(67)

                # Set labels and title with white color for visibility on dark background
                ax.set_xlabel('Proportion (%)', color='white')
                ax.set_ylabel(' ', color='black')
                ax.set_title('Sentiment Analysis Proportion', color='white')

                # Change the color of all tick labels to white
                for label in ax.get_xticklabels() + ax.get_yticklabels():
                    label.set_color('white')

                plt.tight_layout()
                st.pyplot(fig)
                bar.progress(100)
            else:
                st.write("No posts found for the given cryptocurrency ⛔ ")
                
elif page == 'Global Trends 🌍💱':
    st.title("Analyze Global Cryptocurrency Market Sentiment 🌍💱")
    if st.button("Analyze Global Sentiment 🕵️"):
        with st.spinner("🌐 Fetching latest posts and analyzing sentiment..."):
            # Initialize progress
            bar = st.progress(0)


            bar=st.progress(100)
        
    
 
elif page == "Search by SubReddit 📂":
    st.title("Analyze CryptoCurrency Sentiment by SubReddit 📂")




    # User inputs for subreddit selection and optional keyword filtering
    subreddit_input = st.text_input("🔍🌐 Enter the subreddit name (e.g., CryptoCurrency):", value="CryptoCurrency")
    keyword_input = st.text_input("🔑 Enter a keyword to filter (optional):", value="")
    limit_posts = st.number_input("Number of posts to analyze:", min_value=5, max_value=50, value=15, step=5)
    
    if st.button("Analyze Sentiment 🕵️"):
        with st.spinner("🌐 Fetching latest posts and analyzing sentiment..."):
            # Initialize progress
            bar = st.progress(0)

            # Fetch posts using the existing function with the user's input
            # If keyword is not provided (empty string), it fetches the latest posts regardless of keywords
            posts = fetch_reddit_posts(subreddit=subreddit_input, keyword=keyword_input, limit=limit_posts)
            bar.progress(33)  # Update progress after fetching posts

            if posts:
                time.sleep(1)  # Simulate processing time
                sentiment_results = analyze_sentiment(posts)
                bar.progress(67)  # Update progress after analyzing sentiment

                # Map model output to readable sentiments
                label_map = {'LABEL_0': 'Bullish', 'LABEL_1': 'Neutral', 'LABEL_2': 'Bearish'}
                sentiment_results['label'] = sentiment_results['label'].map(lambda x: label_map.get(x, x))
                
                # Calculate and display sentiment probabilities
                sentiment_probs = sentiment_results['label'].value_counts(normalize=True) * 100
                sentiment_colors = {'Bullish': 'green', 'Neutral': '#FAA300', 'Bearish': 'red'}

                st.write(sentiment_probs)

                # Use a horizontal bar plot
                fig, ax = plt.subplots(facecolor='#0B0E12')
                sentiment_probs.plot(kind='barh', color=[sentiment_colors[label] for label in sentiment_probs.index], ax=ax)

                # Set the properties of the axes
                ax.set_facecolor('#0B0E12')
                ax.tick_params(colors='white', which='both')
                ax.spines['bottom'].set_color('black')
                ax.spines['left'].set_color('black')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                # Set labels and title with white color for visibility on dark background
                ax.set_xlabel('Proportion (%)', color='white')
                ax.set_ylabel(' ', color='black')
                ax.set_title('Sentiment Analysis Proportion', color='white')

                # Change the color of all tick labels to white
                for label in ax.get_xticklabels() + ax.get_yticklabels():
                    label.set_color('white')

                plt.tight_layout()
                st.pyplot(fig)

                bar.progress(100)  # Complete the progress
            else:
                st.write("No posts were fetched, please check the subreddit name or try a different keyword.")



    # Reference
    st.markdown("Reference: ElKulako (2022). CryptoBERT: A Pre-trained NLP Model for Cryptocurrency Sentiment Analysis. IEEE Explore. Available at: [IEEE Xplore](https://ieeexplore.ieee.org/document/10223689)")


