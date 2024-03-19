Cryptocurrency Sentiment Analysis
This project utilizes Streamlit to create a web application that analyzes the sentiment of cryptocurrency-related posts on Reddit. By leveraging the CryptoBERT model, the app can determine whether the overall sentiment of a post is bullish, neutral, or bearish. This tool can be invaluable for traders, investors, and cryptocurrency enthusiasts who want to gauge market sentiment and make informed decisions.

Features
Search by Token: Allows users to enter a cryptocurrency symbol (e.g., $BTC, $ETH, $ADA) to fetch and analyze sentiment from relevant Reddit posts.
Search by SubReddit: Users can specify a subreddit and optionally filter by a keyword to analyze sentiment in posts.
Global Trends: Offers an overview of the global sentiment towards cryptocurrencies based on the latest posts from selected subreddits.
Technologies Used
Python
Streamlit
Pandas
Matplotlib
Transformers (Hugging Face)
PRAW (Python Reddit API Wrapper)
Setup and Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
This command will install all necessary Python packages including Streamlit, Pandas, Matplotlib, Transformers, and PRAW.

Run the Streamlit app:
bash
Copy code
streamlit run app.py
Replace app.py with the name of your main Python script.

Configuration
Before using the app, you'll need to configure your Reddit API credentials. Edit the reddit object initialization in the code with your client_id, client_secret, and user_agent.

python
Copy code
reddit = Reddit(client_id='your_client_id',
                client_secret='your_client_secret',
                user_agent='your_user_agent')
How to Use
Navigate through the app using the sidebar to choose between different analysis options. Enter the required information based on your selection and click the "Analyze Sentiment" button to view the results.

Contribution
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

License
MIT

Acknowledgements
This project uses CryptoBERT, a pre-trained NLP model for cryptocurrency sentiment analysis, developed by ElKulako. Reference: ElKulako (2022). CryptoBERT: A Pre-trained NLP Model for Cryptocurrency Sentiment Analysis. IEEE Explore.

Disclaimer
This project is for informational purposes only and should not be considered financial advice.
